# Higher Lower
from art import *
from game_data import data
from random import randint
from clearout import clear

points = 0
answer = True
currentPerson = randint(0, len(data)-1)

while answer:
    print(logo)
    # I could use choice() but I chose randint instead

    randomPerson = randint(0, len(data)-1)
    print(f"Your current score is: {points}")
    print(
        f"Compare A: {data[currentPerson]['name']} , {data[currentPerson]['description']} , {data[currentPerson]['country']}")

    print(vs)

    print(
        f"Compare B: {data[randomPerson]['name']} , {data[randomPerson]['description']} , {data[randomPerson]['country']}")

    while True:
        A = data[currentPerson]['follower_count']
        B = data[randomPerson]['follower_count']
        # using max() compare A and B and gets the highest value
        Highest = max(A, B)
        who_has_more = input(
            "Who has more followers? Type 'A' or 'B': ").upper()

    # if I say A and A is False than you lose

        if who_has_more == 'A' and Highest == A:
            currentPerson = randomPerson
            clear()
            points += 1
            print(f"Correct! your total score is {points} ")
            break
        elif who_has_more == 'B' and Highest == B:
            currentPerson = randomPerson
            clear()
            points += 1
            print(f"Correct! your total score is {points} ")
            break
        else:
            clear()
            print(logo)
            print(
                f"Sorry your answer is not correct, total score {points}, Game Over ")
            exit()
