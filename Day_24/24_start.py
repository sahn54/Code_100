with open("Code_100/Day_24/my_file.txt") as file:
    contents = file.read()
    print(contents)


with open("Code_100/Day_24/new_file.txt", mode="w") as file:
    file.write("New text.")
