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

formatted_list_numbers_a = [f"{number:,}" for number in list_of_numbers_a]

formatted_expected_a = [f"{number:,}" for number in expected_a]

formatted_user_responses_a = [f"{number:,}" for number in responses_list_a]

section_b, topic_b, list_of_numbers_b, unit, values_list_b, responses_list_b, results_b, points_earned_b, total_points_b = rounding_range_quiz.main()

formatted_list_numbers_b = [f"{number:,}" for number in list_of_numbers_b]

formatted_expected_b = [f"{num1:,}, {num2:,}" for (num1, num2) in values_list_b]

formatted_user_responses_b = [f"{num1:,}, {num2:,}" for (num1, num2) in responses_list_b]

def display_results():
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


def file_output(filename):
    
    with open(filename, "a") as file:
        file.write(f"\n\n**{username} | {formatted_date}**\n")
        file.write(f"{'Topic:':<25} {section_a}\n")
        file.write(f"{'List of numbers:':<25} {formatted_list_numbers_a}\n")
        file.write(f"{'Expected answers:':<25} {formatted_expected_a}\n")
        label = f"{username}'s answers:"
        file.write(f"{label:<25} {formatted_user_responses_a}\n")
        file.write(f"Section A: {points_earned_a} / {total_points_a}\n")
        file.write(f"{'Topic: ':<25} {section_b}\n")
        file.write(f"{'List of numbers:':<25} {formatted_list_numbers_b}\n")
        file.write(f"{'Expected answers:':<25} {formatted_expected_b}\n")
        file.write(f"{label:<25} {formatted_user_responses_b}\n")
        file.write(f"Section B: {points_earned_b} / {total_points_b}\n")
        points_earned_total, max_points, grade = display_results()
        file.write(f"Final results: {points_earned_total} / {max_points}: Grade {grade}\n")
                   


file_output("log.md")

'''
def remove_content(filename):
    with open(filename, "w") as file:
        file.write("")

remove_content("example.txt")
'''

