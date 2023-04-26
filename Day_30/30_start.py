# Errors and Exception
# with open("Code_100/Day_30/a-file.txt")as file :
#     file.read()

# KeyError
# a_dictionary = {"key" :"value"}
# value = a_dictionary["non_existent_key"]


# #IndexError
# fruit_list = ["Apple", "Bannana", "Pear"]
# fruit = fruit_list[3]

# TypeError
# text = "abc"
# print(text + 5)


# try : Something that might cause an exception

# try:
#     file = open("a_file.txt")
#     a_dictionary = {"key": "value"}
#     print(a_dictionary["sdfsdf"])

# # except: Do this if there was an exception
# except FileNotFoundError:
#     file = open("a_file.txt", "w")
#     file.write("Something")
# except KeyError as error_message:
#     print(f"The key {error_message} does not exist.")

# # else; Do this there were no exception
# else:
#     content = file.read()
#     print(content)
# finally: Do this no matter what happens
# finally:
# raise TypeError("This is an error that I made up.")
# file.close()
# print("File was closed. ")

height = float(input("Height: "))
weight = int(input("weight: "))

if height > 3:
    raise ValueError("Human Height should not be over 3 meters.")


bmi = weight / height ** 2
print(bmi)
