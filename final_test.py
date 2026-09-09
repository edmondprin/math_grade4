# calculate_final_results() → returns a new value (a dictionary).
# format_numbers(section_1) → mutates an existing Python object.
# save_report() / remove_content() → causes an external side effect by changing a file

import rounding_quiz
import rounding_range_quiz
import datetime


def gather_test_data():
    today = datetime.datetime.now()
    username = input("Enter your name: ")
    return {
        'name' : username.title().strip(),
        'date' : today.strftime("%m/%d/%Y")
    }


def format_numbers(section_1):
    section_1['numbers_generated']= [f"{number:,}" for number in section_1['numbers_generated']]
    section_1['expected_numbers'] = [f"{number:,}" for number in section_1['expected_numbers']]
    section_1['user_answers'] = [f"{number:,}" for number in section_1['user_answers']]
    return section_1


def format_ranges(section_2):
    section_2['numbers_generated'] = [f"{number:,}" for number in section_2['numbers_generated']]
    section_2['expected_numbers'] = [f"{num1:,}, {num2:,}" for (num1, num2) in section_2['expected_numbers']]
    section_2['user_answers'] = [f"{num1:,}, {num2:,}" for (num1, num2) in section_2['user_answers']]
    return section_2


def calculate_final_results(points_earned_a, points_earned_b, total_points_a, total_points_b):
    points_earned_total = points_earned_a + points_earned_b
    max_points = total_points_a + total_points_b
    percent = points_earned_total / max_points
    if percent >= 0.9:
        grade = "A"
    elif percent >= 0.75:
        grade = "B"
    elif percent >= 0.6:
        grade = "C"
    elif percent >= 0.5:
        grade = "D"
    elif percent >= 0.35:
        grade = "E"
    else:
        grade = "F"
    return {
        'points': points_earned_total, 
        'total_questions': max_points, 
        'final_grade': grade
    }


def build_report(user_data, section_1, section_2, total):
    report = f"\n\n**{user_data['name']} | {user_data['date']}**\n"
    report += f"{'Topic:':<25} {section_1['section']}\n"
    report += f"{'List of numbers:':<25} {section_1['numbers_generated']}\n"
    report += f"{'Expected answers:':<25} {section_1['expected_numbers']}\n"

    label = f"{user_data['name']}'s answers:"
    report += f"{label:<25} {section_1['user_answers']}\n"
    report += f"Section A: {section_1['points']} / {section_1['total_questions']}\n"

    report += f"{'Topic:':<25} {section_2['section']}\n"
    report += f"{'List of numbers:':<25} {section_2['numbers_generated']}\n"
    report += f"{'Expected answers:':<25} {section_2['expected_numbers']}\n"

    report += f"{label:<25} {section_2['user_answers']}\n"
    report += f"Section B: {section_2['points']} / {section_2['total_questions']}\n"

    report += f"Total results: {total['points']} / {total['total_questions']} | Grade: {total['final_grade']}"
    
    return report


def save_report(filename, report):
    with open(filename, "a") as file:       
        file.write(report)


def main():
    # today, username = gather_test_data()
    # formatted_date = 
    user_data = gather_test_data()

    section_1 = rounding_quiz.main()
    # print(section_1)
    # print(section_1['section'])
    # print(section_1['expected_answers'])

    format_numbers(section_1)
    # print(section_1)

    section_2 = rounding_range_quiz.main()
    format_ranges(section_2)
    # print(section_2)


    total = calculate_final_results(section_1['points'], section_2['points'], section_1['total_questions'], section_2['total_questions'])



    report = build_report(user_data, section_1, section_2, total)
    save_report("log.md", report)


if __name__ == "__main__":
    main()
    

'''
def remove_content(filename):
    with open(filename, "w") as file:
        file.write("")

remove_content("example.txt")


section
numbers_generated
expected_numbers
user_answers
points
total_questions
'''