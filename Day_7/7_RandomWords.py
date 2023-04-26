# Step 1
import random

word_list = ["aardvark", "baboon", "camel"]

# TODO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word.

word = random.randint(0, len(word_list)-1)
chosen_Word = word_list[word]

# TODO-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.
guess = input("Enter a letter: ")
guess = guess.lower()


# TODO-3 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word.

num = 0
for letter in range(0, len(chosen_Word)):
    if guess == chosen_Word[num]:
        print("Right")
        num += 1
    else:
        print("Wrong")
        num += 1
