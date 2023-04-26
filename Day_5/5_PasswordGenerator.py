import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
           'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

password_list = []
password = ""
for letter in range(1, nr_letters+1):
    letter_password = random.randint(0, len(letters)-1)
    letter = letters[letter_password]
    password_list.append(letter)
for number in range(1, nr_numbers+1):
    number_password = random.randint(0, len(numbers)-1)
    number = numbers[number_password]
    password_list.append(number)
for symbol in range(1, nr_symbols+1):
    symbol_password = random.randint(0, len(symbols)-1)
    symbol = symbols[symbol_password]
    password_list.append(symbol)

random.shuffle(password_list)
for item in password_list:
    password += item
print(f"Your Password is : {password}")
