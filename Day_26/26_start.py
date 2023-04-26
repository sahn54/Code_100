# List Comprehension
# new_list = [new_item for item in list]
# Can be used in a list or string


# Example:
# name = "Sung"
# new_list = [letter for letter in name]
# Answer:
# ['S','u','n','g']

# Create a new list from a range, where the list items are double the values in the range
# range (1,5)
# Answer:
# range_list =[num * 2 for num in range(1,5)]

# Conditional List Comprehension
# new_list = [new_item for item in list if test]

# Example:
# names = ["Alex", "Beth" , "Caroline", "Dave", "Elanor", "Freddie"]
# short_names = [name for name in names if len(name) < 5]

# Create a new list that contains the names longer than 5 characters in ALL CAPS.
# cap_names = [name.upper() for name in names if len(name) > 5]
# print(cap_names)
# ['CAROLINE', 'ELANOR', 'FREDDIE']
