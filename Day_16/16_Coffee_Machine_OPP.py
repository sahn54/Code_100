from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


my_menu = Menu()
my_CoffeeMaker = CoffeeMaker()
coins = MoneyMachine()

machine_on = True
while machine_on:

    user_choice = input(
        f"What would you like? ({my_menu.get_items()}​) :").lower()

    if user_choice == "off":
        machine_on = False
    elif user_choice == "report":
        my_CoffeeMaker.report()
        coins.report()
    elif user_choice == "espresso" or user_choice == "latte" or user_choice == "cappuccino":
        user_drink = my_menu.find_drink(user_choice)
        check_machine = my_CoffeeMaker.is_resource_sufficient(user_drink)
        # if check_machine and coins.make_payment(user_drink.cost):
        #     my_CoffeeMaker.make_coffee(user_drink)
    else:
        continue
