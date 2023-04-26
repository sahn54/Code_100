# Coffee Machine Project


# 1. 3 hot flavors
# Espresso = 50ml
# Latte
# Cappuccino

# 2. Coin Operated
# Penny = 0.01
# Nickel = 0.05
# Dime = 0.10
# Quarter = 0.25

# a. print report.
# b. check resources sufficient?
# c. process coins
# d. check transaction successful?
# e. Make coffee

from coffee_data import *


def check_resources(order):

    if resources['water'] < MENU[order]['ingredients']['water']:
        print("Sorry there is not enough water.")
        return False
    elif resources['milk'] < MENU[order]['ingredients']['milk']:
        print("Sorry there is not enough milk.")
        return False
    elif resources['coffee'] < MENU[order]['ingredients']['coffee']:
        print("Sorry there is not enough milk.")
        return False
    else:
        return True


def insertCoin():
    print("Please insert coins:")
    q = int(input("How many quarters? "))
    q *= 0.25
    d = int(input("How many dimes? "))
    d *= 0.10
    n = int(input("How many nickles? "))
    n *= 0.05
    p = int(input("How many pennies? "))
    p *= 0.01
    coins = q + d + n + p
    # print(round(coins, 2))
    return coins


def transaction(machineInput, inputCoins):
    if inputCoins >= MENU[machineInput]['cost']:
        bank["money"] += MENU[machineInput]['cost']
        change = inputCoins - MENU[machineInput]['cost']
        if change != 0.00:
            print(f"Here is ${round(change,2):.2f} in change")
        make_coffee(machineInput)
    else:
        print("Sorry that's not enough, Money refunded. ")
    return bank["money"]


def make_coffee(machineInput):
    resources['water'] -= MENU[machineInput]['ingredients']['water']
    resources['milk'] -= MENU[machineInput]['ingredients']['milk']
    resources['coffee'] -= MENU[machineInput]['ingredients']['coffee']
    print(f"Here is your {machineInput}. Enjoy!")


machine_on = True


while machine_on:
    machineInput = input(
        "What would you like? (espresso/latte/cappuccino): ").lower()

    if machineInput == "off":
        machine_on = False

    elif machineInput == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${bank['money']:.2f}")

    elif machineInput == "espresso" or machineInput == "latte" or machineInput == "cappuccino":
        required_resources = check_resources(machineInput)
        if required_resources:
            coins_added = insertCoin()
            transaction(machineInput, coins_added)

    else:
        continue
