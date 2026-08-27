import random

# tens, hundreds, thousands choice
# create original list
# gather user input
# check answer
# round (x, -1): tens
# round (x, -2): hundreds
# round (x, -3): thousands
# round (x, -4): tens of thousands
# round (x, -5): hundreds of thousands
# round (x, -6): millions
# when in middle, go to nearest high?


def pick_a_topic():
    options_list = ["tens", "hundreds", "thousands", "tens of thousands", "hundreds of thousands", "millions"]
    return random.choice(options_list)

def create_numbers_list():
    option = pick_a_topic()
    your_range = 3
    numbers_list = []
    for _ in range(your_range):
        if option == "tens":
            x = random.randint(0, 100)
        elif option == "hundreds":
            x = random.randint(100, 999)
        elif option == "thousands":
            x = random.randint(1000, 9999)
        elif option == "tens of thousands":
            x = random.randint(10000, 99999)
        elif option == "hundreds of thousands":
            x = random.randint(100000, 999999)
        else:
            x = random.randint(1000000, 9999999)
        numbers_list.append(x)
    return option, numbers_list, len(numbers_list)

def gather_answer():
    topic, tested_list, length = create_numbers_list()
    user_responses = []
    for _ in range(length):
        while True:
            user_input = input(f"What is the nearest {topic} for {tested_list[_]}? ")
            try:
                user_input = int(user_input)
                user_responses.append(user_input)
                break
            except ValueError:
                print("You need to enter a number!")
    return topic, tested_list, user_responses


def check_answers():
    topic, tested_list, user_responses = gather_answer()
    results = []
    if topic == "tens":
        expected = list(map(lambda x: round(x, -1), tested_list))
    if topic == "hundreds":
            expected = list(map(lambda x: round(x, -2), tested_list))
    if topic == "thousands":
            expected = list(map(lambda x: round(x, -3), tested_list))
    if topic == "tens of housands":
            expected = list(map(lambda x: round(x, -4), tested_list))
    if topic == "hundreds of thousands":
            expected = list(map(lambda x: round(x, -5), tested_list))
    if topic == "millions":
            expected = list(map(lambda x: round(x, -6), tested_list))
    for _ in range(len(tested_list)):
        results.append(expected[_] == user_responses[_])
    return results


print(check_answers())