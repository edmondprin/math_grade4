import pytest
from final_test import calculate_final_results


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


@pytest.mark.parametrize(
    "inputs, expected",
    [
        ((1, 0, 10, 10), (1, 20, "F")),
        ((49, 50, 50, 50), (99, 100, "A")),
        ((25, 25, 50, 50), (50, 100, "D"))

        ]
)

def test_calculate_results(inputs, expected):
    outcome = calculate_final_results(*inputs)
    assert outcome["points"] == expected[0]
    assert outcome["total_questions"] == expected[1]
    assert outcome["final_grade"] == expected[2]
