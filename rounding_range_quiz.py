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


def pick_number(topic):
    number = random.randint(TOPICS[topic]["number_range"][0], TOPICS[topic]["number_range"][1])
    unit = 10 ** abs(TOPICS[topic]["rounding_place"])
    rounded_number = ((number + unit // 2) // unit) * unit
    return number, rounded_number, unit


def calculate_two_values(target, unit):
    # values_list = []
    min_value = int(target - unit / 2)
    max_value = int(target + unit / 2 - 1)
    # values_list.append((min_value, max_value))
    return min_value, max_value

def gather_answers(topic, number):
    while True:
        min_answer = input(f"There were approximatively {number:,} people at the stadium, rounded to the nearest {topic}. What is the MINIMUM possible actual attendance? ")
        max_answer = input(f"There were approximatively {number:,} people at the stadium, rounded to the nearest {topic}. What is the MAXIMUM possible actual attendance? ")
        clean_min_answer = min_answer.replace(",","")
        clean_max_answer = max_answer.replace(",","")
        try:
            clean_min_answer = int(clean_min_answer)
            clean_max_answer = int(clean_max_answer)
            break
        except ValueError:
            print("You need to enter a number!")
    return clean_min_answer, clean_max_answer

def check_answers(topic, number):
    pass

def main():
    topic = pick_topic()
    print(topic)
    this_number, this_rounded_number, unit = pick_number(topic)
    print("raw_number:", this_number, "rounded_number:", this_rounded_number, "unit:", unit)
    lower_end, upper_end = calculate_two_values(this_rounded_number, unit)
    print(lower_end, upper_end)
    mini, maxi = gather_answers(topic, this_rounded_number)
    print(mini, maxi)



if __name__ == "__main__":
    main()