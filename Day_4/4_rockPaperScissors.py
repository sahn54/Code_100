import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

# Write your code below this line 👇

rock_paper_scissors = [rock, paper, scissors]

# User
user_choice = int(
    input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors."))

if user_choice >= 3 or user_choice < 0:
    print("You typed an invaild number, you lose!")
else:
    print(f"Your Choice: \n {rock_paper_scissors[user_choice]}")


# Computer
    computer_randomChoice = random.randint(0, 2)
    print(
        f"Computer chose: \n {rock_paper_scissors[computer_randomChoice]}")

    if user_choice == computer_randomChoice:
        print("You Tied")
    elif ((user_choice == 0) and (computer_randomChoice == 1)) or ((user_choice == 1) and (computer_randomChoice == 2)) or ((user_choice == 2) and (computer_randomChoice == 3)):
        print("You lose")
    elif ((user_choice == 0) and (computer_randomChoice == 2)) or ((user_choice == 1) and (computer_randomChoice == 0)) or ((user_choice == 2) and (computer_randomChoice == 1)):
        print("You win!")
