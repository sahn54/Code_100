# example extended version 2:
# Nested if / else


print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
bill = 0
if height >= 120:
    print("You can ride the rollercoaster.")
    age = int(input("What is your age? "))
    if age < 12:
        bill = 5
        print("Please pay $5")
    elif age <= 18:
        bill = 7
        print("Please pay $7")
    elif 55 >= age >= 45:
        print("Everything is going to be okay! Have a free ride on us!")
    else:
        bill = 12
        print("Please pay $12")

    want_photo = input("Would like a photo? ")
    if want_photo == "Y" or want_photo == "y":
        bill += 3

    print(f"Your final bill is ${bill}")

else:
    print("Sorry, you have to grow taller before you can ride.")
