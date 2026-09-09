import rounding_quiz
import rounding_range_quiz
import datetime


def gather_test_data():
    today = datetime.datetime.now()
    username = input("Enter your name: ")
    return today, username.title().strip() 


def format_numbers(list_of_numbers_a, expected_a, responses_list_a):
    formatted_list_numbers_a = [f"{number:,}" for number in list_of_numbers_a]
    formatted_expected_a = [f"{number:,}" for number in expected_a]
    formatted_user_responses_a = [f"{number:,}" for number in responses_list_a]
    return formatted_list_numbers_a, formatted_expected_a, formatted_user_responses_a


def format_ranges(list_of_numbers_b, values_list_b, responses_list_b):
    formatted_list_numbers_b = [f"{number:,}" for number in list_of_numbers_b]
    formatted_expected_b = [f"{num1:,}, {num2:,}" for (num1, num2) in values_list_b]
    formatted_user_responses_b = [f"{num1:,}, {num2:,}" for (num1, num2) in responses_list_b]
    return formatted_list_numbers_b, formatted_expected_b, formatted_user_responses_b


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
    return points_earned_total, max_points, grade

'''
section_1 = {
"topic: "section_a,
"numbers_generated": formatted_list_numbers_a,
"expected_numbers": formatted_expected_a,
"user_answers": formatted_user_responses_a,
"points": points_earned_a,
"total_questions": total_points_a
}

section_2 = { 
"topic": section_b, 
"numbers_generated": formatted_list_numbers_b, "expected_numbers": formatted_expected_b, "user_answers": formatted_user_responses_b, 
"points": points_earned_b, 
"total_questions": total_points_b 
}

user_data = { 
"name": username, 
"date": formatted_date 
} 

total = { 
"points": points_earned_total, 
"total_questions": max_points, 
"final_grade": grade 
}
'''

def build_report(user_data, section_1, section_2, total):
    report = f"\n\n**{user_data['name']} | {user_data['date']}**\n"
    report += f"{'Topic:':<25} {section_1['topic']}\n"
    report += f"{'List of numbers:':<25} {section_1['numbers_generated']}\n"
    report += f"{'Expected answers:':<25} {section_1['expected_numbers']}\n"

    label = f"{user_data['name']}'s answers:"
    report += f"{label:<25} {section_1['user_answers']}\n"
    report += f"Section A: {section_1['points']} / {section_1['total_questions']}\n"

    report += f"{'Topic:':<25} {section_2['topic']}\n"
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
    today, username = gather_test_data()
    formatted_date = today.strftime("%m/%d/%Y")

    section_a, list_of_numbers_a, expected_a, responses_list_a, points_earned_a, total_points_a = rounding_quiz.main()

    formatted_list_numbers_a, formatted_expected_a, formatted_user_responses_a = format_numbers(
            list_of_numbers_a,
            expected_a,
            responses_list_a
    )

    section_b, list_of_numbers_b, unit, values_list_b, responses_list_b, points_earned_b, total_points_b = rounding_range_quiz.main()

    formatted_list_numbers_b, formatted_expected_b, formatted_user_responses_b = format_ranges(
            list_of_numbers_b,
            values_list_b,
            responses_list_b
        )

    points_earned_total, max_points, grade = calculate_final_results(points_earned_a, points_earned_b, total_points_a, total_points_b)

    report = build_report(username, section_a, formatted_date, formatted_list_numbers_a, formatted_expected_a, formatted_user_responses_a, points_earned_a, total_points_a, section_b, formatted_list_numbers_b, formatted_expected_b, formatted_user_responses_b, points_earned_b, total_points_b, points_earned_total, max_points, grade)
    save_report("log.md", report)


if __name__ == "__main__":
    main()
    

'''
def remove_content(filename):
    with open(filename, "w") as file:
        file.write("")

remove_content("example.txt")
'''

