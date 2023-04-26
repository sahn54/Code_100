import random

# Introduction of the Number Guessing Game
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")


# setting the random number to guess.
final_answer = random.randint(1, 101)

# checking the difficulty: if non of the answer are easy or hard, it will repeat the question
while True:
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
    if difficulty == 'easy':
        attempt = 10
        break
    elif difficulty == 'hard':
        attempt = 5
        break
    else:
        continue

# not a really important it can be changed
user_attempt = attempt


# checking answer function if the number is low or high. If the number the correct number it will give a winning message and exit.
def check_answer():
    if final_answer > userguess:
        print("Too low")
        return user_attempt - 1

    elif final_answer < userguess:
        print("Too High")
        return user_attempt - 1

    else:
        print(f"You got it! The answer was {final_answer}.")
        print("Guess again.")
        return -1
        # returning -1 since 0 is used for run out of guesses.


# check user_attempts until reaches to 0
while user_attempt > 0:
    print(f"You have {user_attempt} attempts remaining to guess the number.")
    userguess = int(input("Make a guess: "))
    user_attempt = check_answer()
# only if user attempt is 0, it will give out message that you lose.
if user_attempt == 0:
    print("You've run out of guesses, you lose.")
