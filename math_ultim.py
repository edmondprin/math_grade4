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
    for number in range(len(numbers)):
        while True:
            answer = input(f"What is the nearest {topic} for {numbers[number]:,}? ")
            try:
                answer = int(answer)
                responses.append(answer)
                break
            except ValueError:
                print("You need to enter a number!")
    return responses


def calculate_answers(topic, numbers):
    results = []
    expected = list(map(lambda x: round(x, ROUNDING_PLACES[topic]), numbers))
    for number in range(len(numbers)):
        results.append(expected[number])
    return results

def check_answers(topic, numbers, responses):
     expected_answers = calculate_answers(topic, numbers)
     return [
          expected == response
          for expected, response in zip(expected_answers, responses)
     ]

def display_results(results):
    points = 0
    for a in results:
        points += 1 if a == True else 0
    print(f"Congrats! You earned a total of {points} points!")

def main():
     topic = pick_topic()
     print(topic)
     numbers = generate_numbers(topic, count=3)
     print(numbers)
     responses = gather_answers(topic, numbers)
     print(f" Responses: {responses}")
     test = calculate_answers(topic, numbers)
     print(test)
     results = check_answers(topic, numbers, responses)
     print(results)
     display_results(results)


if __name__ == "__main__":
    main()