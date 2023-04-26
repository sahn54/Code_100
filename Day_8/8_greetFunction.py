# Review:
# Create a function called greet().
# Write 3 print statements inside the function.
# Call the greet() function and run your code.


def greet(name):
    print(f"Welcome {name}!")
    print(f"How do you do {name}.")
    print(f"Nice to meet you {name}!")


enterName = input("What is your name? ")
greet(enterName)
