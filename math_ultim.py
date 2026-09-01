import random



def pick_topic():
    options_list = ["tens", "hundreds", "thousands", "tens of thousands", "hundreds of thousands", "millions"]
    return random.choice(options_list)

ROUNDING_PLACES = {
     "tens": -1,
     "hundreds": -2,
     "thousands": -3, 
     "tens of thousands": -4,
     "hundreds of thousands": -5,
     "millions": -6
}

NUMBERS_RANGES = {
     "tens": (0, 100),
     "hundreds": (100, 999),
     "thousands": (1000, 9999),
     "tens of thousands": (10000, 99999),
     "hundreds of thousands": (100000, 999999),
     "millions": (1000000, 9999999)
}

def generate_numbers(topic, count=3):
    numbers_list = []
    for _ in range(count):
        number = random.randint(NUMBERS_RANGES[topic][0], NUMBERS_RANGES[topic][1])
        numbers_list.append(number)
    return numbers_list

def gather_answers(topic, numbers):
    responses = []
    for number in numbers:
        while True:
            answer = input(f"What is the nearest {topic} for {number:,}? ")
            try:
                responses.append(int(answer))
                break
            except ValueError:
                print("You need to enter a number!")
    return responses


def calculate_expected_answers(topic, numbers):
    rounding_place = ROUNDING_PLACES[topic]
    return [round(number, rounding_place) for number in numbers]

def check_answers(topic, numbers, responses):
     expected_answers = calculate_expected_answers(topic, numbers)
     return [
          expected == response
          for expected, response in zip(expected_answers, responses)
     ]

def display_results(results):
    points = sum(results)
    print(f"Congrats! You earned a total of {points} points out of {len(results)}!")

def main():
     topic = pick_topic()
    #  print(topic)
     numbers = generate_numbers(topic, count=1)
    #  print(numbers)
     responses = gather_answers(topic, numbers)
    #  print(f" Responses: {responses}")
     test = calculate_expected_answers(topic, numbers)
    #  print(test)
     results = check_answers(topic, numbers, responses)
    #  print(results)
     display_results(results)


if __name__ == "__main__":
    main()