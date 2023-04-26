placeholder = "[name]"

with open("Code_100/Day_24/Mail Merge Project Start/Input/Names/invited_names.txt") as name_files:
    Names = name_files.readlines()
with open("Code_100/Day_24/Mail Merge Project Start/Input/Letters/starting_letter.txt") as letter_files:
    letter_content = letter_files.read()
    for name in Names:
        striped_name = name.strip("\n")
        new_letter = letter_content.replace(placeholder, striped_name)
        print(new_letter)
        with open(f"Code_100/Day_24/Mail Merge Project Start/Output/ReadyToSend/letter_for_{striped_name}.txt", mode="w") as DUN_letters:
            DUN_letters.write(new_letter)
