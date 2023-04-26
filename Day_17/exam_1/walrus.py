# Write a program that repeatedly reads integers from the user and calculates their sum, until the user enters a negative number. Use the walrus operator to assign the input value to a variable within the while loop.
def walrus_sum():
    w_sum = 0
    while (num := int(input("Enter a number: "))) >= 0:
        w_sum += num
    print(f"Input is {w_sum}")


walrus_sum()
# Write a program that reads a string from the user and determines whether it contains any digits. Use the walrus operator to assign the result of the isdigit() method to a variable within the if statement.

# Write a program that reads a list of numbers from the user and computes their average, ignoring any negative numbers. Use the walrus operator to assign the sum of the non-negative numbers to a variable within the for loop.

# Write a program that reads a sentence from the user and counts the number of words that contain the letter 'e'. Use the walrus operator to assign the result of the count() method to a variable within the list comprehension.

# Write a program that reads a list of strings from the user and removes any duplicates, while preserving the original order of the elements. Use the walrus operator to assign the boolean value True to the condition s not in seen for each element s in the list.


# Example 1
while (n := len(input())) > 0:
    print(f"Input string length is {n}")
# Example 2
user_input = input("Enter a number: ")
if (number := int(user_input)) % 2 == 0:
    print(f"{number} is even.")
else:
    print(f"{number} is odd.")
# Example 3
# numbers = [10, 20, 30, 40, 50]
# even_numbers = [n for n in numbers if (n % 2 == 0) := True]
# print(even_numbers)
