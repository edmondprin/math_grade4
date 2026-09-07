import rounding_quiz
import rounding_range_quiz
import datetime

def gather_test_data():
    today = datetime.datetime.now()
    name = input("Enter your name: ")
    return today, name.title().strip()

today, username = gather_test_data()
formatted_date = today.strftime("%m/%d/%Y")


section_a, topic_a, list_of_numbers_a, expected_a, responses_list_a, results_a, points_earned_a, total_points_a = rounding_quiz.main()

def format_numbers(list_of_numbers_a, expected_a, responses_list_a):
    formatted_list_numbers_a = [f"{number:,}" for number in list_of_numbers_a]
    formatted_expected_a = [f"{number:,}" for number in expected_a]
    formatted_user_responses_a = [f"{number:,}" for number in responses_list_a]
    return formatted_list_numbers_a, formatted_expected_a, formatted_user_responses_a

section_b, topic_b, list_of_numbers_b, unit, values_list_b, responses_list_b, results_b, points_earned_b, total_points_b = rounding_range_quiz.main()

def format_ranges(list_of_numbers_b, values_list_b, responses_list_b):
    formatted_list_numbers_b = [f"{number:,}" for number in list_of_numbers_b]
    formatted_expected_b = [f"{num1:,}, {num2:,}" for (num1, num2) in values_list_b]
    formatted_user_responses_b = [f"{num1:,}, {num2:,}" for (num1, num2) in responses_list_b]
    return formatted_list_numbers_b, formatted_expected_b, formatted_user_responses_b

def calculate_final_results():
    points_earned_total = points_earned_a + points_earned_b
    max_points = total_points_a + total_points_b
    percent = points_earned_total / max_points
    if percent > 0.9:
        grade = "A"
    elif percent >= 0.75:
        grade = "B"
    elif percent > 0.6:
        grade = "C"
    elif percent > 0.5:
        grade = "D"
    elif percent > 0.35:
        grade = "E"
    else:
        grade = "F"
    return points_earned_total, max_points, grade


def build_report():
    formatted_list_numbers_a, formatted_expected_a, formatted_user_responses_a = format_numbers(
        list_of_numbers_a,
        expected_a,
        responses_list_a
    )

    formatted_list_numbers_b, formatted_expected_b, formatted_user_responses_b = format_ranges(
        list_of_numbers_b,
        values_list_b,
        responses_list_b
    )

    points_earned_total, max_points, grade = calculate_final_results()

    report = f"\n\n**{username} | {formatted_date}**\n"
    report += f"{'Topic:':<25} {section_a}\n"
    report += f"{'List of numbers:':<25} {formatted_list_numbers_a}\n"
    report += f"{'Expected answers:':<25} {formatted_expected_a}\n"

    label = f"{username}'s answers:"
    report += f"{label:<25} {formatted_user_responses_a}\n"
    report += f"Section A: {points_earned_a} / {total_points_a}\n"

    report += f"{'Topic:':<25} {section_b}\n"
    report += f"{'List of numbers:':<25} {formatted_list_numbers_b}\n"
    report += f"{'Expected answers:':<25} {formatted_expected_b}\n"
    
    label = f"{username}'s answers:"
    report += f"{label:<25} {formatted_user_responses_b}\n"
    report += f"Section B: {points_earned_b} / {total_points_b}\n"

    report += f"Total results: {points_earned_total} / {max_points} | Grade: {grade}"

    return report

def save_report(filename, report):
    with open(filename, "a") as file:
        file.write(report)

report = build_report()
save_report("log.md", report)


'''
def remove_content(filename):
    with open(filename, "w") as file:
        file.write("")

remove_content("example.txt")
'''

