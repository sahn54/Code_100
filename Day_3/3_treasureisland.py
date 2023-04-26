print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')


print("Welcome to Tresure Island.")
print("Your mission is to find the treasure.")


crossRoad = input(
    'You are at a cross road. Where do you want to go? Type "left" or "right"')
crossRoad = crossRoad.lower()
if crossRoad == "right":
    print("You died. ")
elif crossRoad == "left":
    lake = input('You come to a lake. There is an island in the middle of the lake. Type "Wait" to wait for a boat. Type "swim" to swim across. ')
    lake = lake.lower()
    if lake == "swim":
        print("You died")
    elif lake == "wait":
        island = input(
            'You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. Which colour do you choose? ')
        island = island.lower()
        if island == "red":
            print("Game over")
        elif island == "blue":
            print("You died")
        elif island == "green":
            print("You win!")
        else:
            print("Game over")
    else:
        print("Game over")
else:
    print("Error")

print("Thank you for playing!")
