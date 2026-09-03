import random

TOPICS = {
    "tens": {
        "rounding_place": -1,
        "number_range": (10, 100),
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


def pick_number(topic, count=5):
    numbers_list = []
    for _ in range(count):
        while True:
            print(_)
            number = random.randint(TOPICS[topic]["number_range"][0], TOPICS[topic]["number_range"][1])
            unit = 10 ** abs(TOPICS[topic]["rounding_place"])
            rounded_number = ((number + unit // 2) // unit) * unit
            if rounded_number not in numbers_list:
                numbers_list.append(rounded_number)
                break
    return numbers_list, unit

def calculate_two_values(numbers, unit):
    values_list = []
    for number in numbers:
        min_value = int(number - unit / 2) 
        max_value = int(number + unit / 2 - 1)
        values_list.append((min_value, max_value))
    return values_list

def gather_answers(topic, numbers):
    responses_list = []
    for number in numbers:
        while True:
            min_answer = input(f"There were approximately {number:,} people at the stadium, rounded to the nearest {topic}. What is the MINIMUM possible actual attendance? ")
            max_answer = input(f"There were approximately {number:,} people at the stadium, rounded to the nearest {topic}. What is the MAXIMUM possible actual attendance? ")
            clean_min_answer = min_answer.replace(",","")
            clean_max_answer = max_answer.replace(",","")
            try:
                clean_min_answer = int(clean_min_answer)
                clean_max_answer = int(clean_max_answer)
                break
            except ValueError:
                print("You need to enter a number!")
        responses_list.append((clean_min_answer, clean_max_answer))
    return responses_list

def check_answers(numbers, responses):
    if len(numbers) != len(responses):
        raise ValueError("Numbers and responses must have the same length.")

    return [
    expected == response 
    for expected, response in zip(numbers, responses)
    ]

def display_results(results):
    points = sum(results)
    print(f"You have a total of {points} points out of {len(results)}")

def main():
    topic = pick_topic()
    print("1:", topic)
    list_of_numbers, unit = pick_number(topic, count=2)
    # print("raw_number:", this_number, "rounded_number:", this_rounded_number, "unit:", unit)
    print("2:", list_of_numbers, unit)
    values_list = calculate_two_values(list_of_numbers, unit)
    print("3: Expected values: ", values_list)
    responses_list = gather_answers(topic, list_of_numbers)
    print("4: User answers: ", responses_list)
    see_results = check_answers(values_list, responses_list)
    print("5:", see_results)
    display_results(see_results)



if __name__ == "__main__":
    main()