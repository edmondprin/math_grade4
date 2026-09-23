import pytest
import datetime
from final_test import calculate_final_results, gather_test_data, format_numbers, format_ranges


# def test_calculate_results():

#     great_student = calculate_final_results(4, 5, 5, 5)
#     assert great_student['points'] == 9
#     assert great_student['total_questions'] == 10
#     assert great_student['final_grade'] == "A"

#     average_student = calculate_final_results(2, 2, 4, 4)
#     assert average_student['points'] == 4
#     assert average_student['total_questions'] == 8
#     assert average_student["final_grade"] == "D"

#     mediocre_student = calculate_final_results(1, 0, 50, 50)
#     assert mediocre_student["points"] == 1
#     assert mediocre_student["total_questions"] == 100
#     assert mediocre_student["final_grade"] == "F"

# returns a new dictionary, tested with parametrization.

@pytest.mark.parametrize(
    "inputs, expected",
    [
        ((1, 0, 10, 10), (1, 20, "F")),
        ((49, 50, 50, 50), (99, 100, "A")),
        ((25, 25, 50, 50), (50, 100, "D"))

        ]
)

def test_calculate_results(inputs, expected):
    outcome = calculate_final_results(*inputs) # tuple unpacking to get 4 values instead of 1
    assert outcome["points"] == expected[0]
    assert outcome["total_questions"] == expected[1]
    assert outcome["final_grade"] == expected[2]

# mutate dictionaries, tested by checking their state after the call.
def test_format_section1():
    my_dict = {
"section": "quizz",
"numbers_generated": [55, 1234],
"expected_numbers": [60, 1200],
"user_answers": [60, 1250],
"points": 1,
"total_questions": 2
}
    my_results = format_numbers(my_dict)
    assert isinstance(my_results["numbers_generated"], list)
    assert my_results["numbers_generated"] == ["55", "1,234"]
    assert my_results["expected_numbers"] == ["60", "1,200"]

# known input → call function → assert exact expected output

def test_format_section2():
    my_dict = {
        "section": "ranges",
        "numbers_generated": [200, 1500],
        "expected_numbers": [(150, 249), (1450, 1549)],
        "user_answers": [(150, 249), (1450, 1549)],
        "points": 2,
        "total_questions": 2
    }
    my_results = format_ranges(my_dict)
    assert my_results["numbers_generated"] == ["200", "1,500"]
    assert my_results["expected_numbers"] == ["150, 249", "1,450, 1,549"]
    assert my_results["user_answers"] == ["150, 249", "1,450, 1,549"]
'''
def test_gather_data():
    date, name = gather_test_data()
    assert isinstance(date, 'datetime.datetime')
    assert not name.isupper()
    '''