import random

TOPICS = {
    "tens": {
        "rounding_place": -1,
        "number_range": (0, 100),
    },
    "hundreds": {
        "rounding_place": -2,
        "number_range": (100, 999),
    },
    "thousands": {
        "rounding_place": -3,
        "number_range": (1000, 9999),
    },
    "tens of thousands": {
        "rounding_place": -4,
        "number_range": (10000, 99999),
    },
    "hundreds of thousands": {
        "rounding_place": -5,
        "number_range": (100000, 999999),
    },
    "millions": {
        "rounding_place": -6,
        "number_range": (1000000, 9999999),
    },
}


def pick_topic():
    return random.choice(list(TOPICS))


def generate_numbers(topic, count=10):
    numbers_list = []
    for _ in range(count):
        number = random.randint(TOPICS[topic]['number_range'][0], TOPICS[topic]['number_range'][1])
        numbers_list.append(number)
    return numbers_list


def gather_answers(topic, numbers):
    responses = []
    for number in numbers:
        while True:
            answer = input(f"\nWhat is the nearest {topic} for {number:,}? ")
            clean_answer = answer.replace(",", "")
            try:
                responses.append(int(clean_answer))
                break
            except ValueError:
                print("You need to enter a number!")
    return responses


def round_half_up(number, place):
    unit = 10 ** abs(place)
    return ((number + unit // 2) // unit) * unit
    # unit = 10 ** abs(place)
    # halfway_point = unit // 2
    # adjusted_number = number + halfway_point
    # rounded_multiple = adjusted_number // unit
    # return rounded_multiple * unit


def calculate_expected_answers(topic, numbers):
    place = TOPICS[topic]["rounding_place"]
    return [round_half_up(number, place) for number in numbers]


def check_answers(topic, numbers, responses):
    if len(numbers) != len(responses):
        raise ValueError("Numbers and responses must have the same length.")

    expected_answers = calculate_expected_answers(topic, numbers)

    return [
        expected == response
        for expected, response in zip(expected_answers, responses)
    ]


def display_results(results):
    points_earned = sum(results)
    total_points = len(results)
    # print(f"Congrats! You earned a total of {points} points out of {len(results)}!")
    return points_earned, total_points

def main():
     section = "Find the nearest rounded number"
     topic = pick_topic()
     list_of_numbers = generate_numbers(topic, count=2)
     expected = calculate_expected_answers(topic, list_of_numbers)
     responses_list = gather_answers(topic, list_of_numbers)
     results = check_answers(topic, list_of_numbers, responses_list)
     points_earned, total_points = display_results(results)

     return {
        'section': section,
        'numbers_generated': list_of_numbers,
        'expected_numbers': expected,
        'user_answers': responses_list,
        'points': points_earned,
        'total_questions': total_points
    }

if __name__ == "__main__":
    main()