def greet(a):
    print(f"Welcome {a}!")
    print(f"How do you do {a}.")
    print(f"Nice to meet you {a}!")


def greet(a, b):
    print(f"Welcome {a}!")
    print(f"What is it like in {b}?")
    print(f"Nice to meet you {a} and you live in {b}!")


person1 = input("What is your name? ")
location1 = input("Where do you live? ")
greet(b=location1, a=person1)
