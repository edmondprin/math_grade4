import random
import rounding_quiz
import rounding_range_quiz

rounding_quiz.main()
rounding_range_quiz.main()

def display_results():
    list_of_numbers, unit = rounding_range_quiz.pick_number(topic, count)
    print(list_of_numbers)

display_results()
# print to file
# total points
# assign grade
