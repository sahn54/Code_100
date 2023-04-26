# Import the random module here
import random
# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆

# Write your code below this line 👇
random_name = random.randint(0, len(names)-1)
# len() begins with 1 so we need to change to 0
person_who_will_pay = names[random_name]
# person_who_will_pay = random.choice(names)
# choice() will randomly pick an element from the list.
print(f"{person_who_will_pay} is going to buy the meal today!")
