import os

print("Welcome to the secret auction program.")


bid_log = {}
still_bidding = True


def find_highest_bid(bidding_record):
    highest_bid = 0
    winner = ""
    for bidder in bidding_record:
        bid_amount = bidding_record[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"The winner is {winner} with a bid of ${highest_bid}")


while (still_bidding):
    name = input("What is your name?: ")
    bid = int(input("What's your bid?: $"))
    bid_log[name] = bid
    other_bid = input(
        "Are there any other bidders? Type 'yes' or 'no'. ").lower()
    if other_bid == 'yes':
        os.system('clear')
    elif other_bid == 'no':
        still_bidding = False
        find_highest_bid(bid_log)
