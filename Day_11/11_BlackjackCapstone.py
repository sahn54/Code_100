# BlackJack
# Bust = Lose - over 21
# Draw
# A = 1 or 11
# K Q J = 10

# Computer if total number is less than 17 Computer must obtain another card.
############### Blackjack Project #####################

# Difficulty Normal 😎: Use all Hints below to complete the project.
# Difficulty Hard 🤔: Use only Hints 1, 2, 3 to complete the project.
# Difficulty Extra Hard 😭: Only use Hints 1 & 2 to complete the project.
# Difficulty Expert 🤯: Only use Hint 1 to complete the project.

############### Our Blackjack House Rules #####################

# The deck is unlimited in size.
# There are no jokers.
# The Jack/Queen/King all count as 10.
# The the Ace can count as 11 or 1.
# Use the following list as the deck of cards:

# The cards in the list have equal probability of being drawn.
# Cards are not removed from the deck as they are drawn.
# The computer is the dealer.
from blackjack_art import logo
import random


def blackjack():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

    user_card_hand = []
    computer_card_hand = []
    user_current_score = 0
    computer_current_score = 0

    print(logo)

    for i in range(2):
        user_card_1 = random.randint(0, len(cards)-1)
        user_current_score += cards[user_card_1]
        user_card_hand.append(cards[user_card_1])

    computer_card_1 = random.randint(0, len(cards)-1)
    computer_current_score += cards[computer_card_1]
    computer_card_hand.append(cards[computer_card_1])

    while user_current_score < 21:
        print(
            f"Your cards: {user_card_hand}, current score: {user_current_score}")
        print(f"Computer's first card: {cards[computer_card_1]}")
        add_card = input(
            "Type 'y' to get another card, type 'n' to pass: ").lower()
        if add_card == 'y':
            user_card = random.randint(0, len(cards)-1)
            user_current_score += cards[user_card]
            user_card_hand.append(cards[user_card])
            if 11 in user_card_hand and user_current_score > 21:
                user_card_hand.remove(11)
                user_card_hand.append(1)
            continue

        elif add_card == 'n':
            break
        else:
            continue
    while computer_current_score < 17:
        computer_card = random.randint(0, len(cards)-1)
        computer_card_hand.append(cards[computer_card])
        computer_current_score += cards[computer_card]
        if 11 in computer_card_hand and computer_current_score > 21:
            computer_card_hand.remove(11)
            computer_card_hand.append(1)
        continue

    print(
        f"Your final hand: {user_card_hand}, final score: {user_current_score}")
    print(
        f"Computer's final card: {computer_card_hand}, final score {computer_current_score}")

    if user_current_score > 21:
        print("You lose")
    elif computer_current_score > 21:
        print("You Win 😃")
    elif user_current_score < computer_current_score:
        print("You lose")
    elif user_current_score > computer_current_score:
        print("You Win 😃")
    else:
        print("Draw")

    # Reset list and score
    user_card_hand = []
    computer_card_hand = []
    user_current_score = 0
    computer_current_score = 0


continue_toPlay = True

while continue_toPlay:
    play_game = input(
        "Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower()
    if play_game == 'y':
        blackjack()
    elif play_game == 'n':
        continue_toPlay = False
    else:
        continue
