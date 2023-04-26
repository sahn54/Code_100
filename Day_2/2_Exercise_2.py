# Life in Weeks
# Create a program using maths and f-Strings that tells us how many days, weeks, months we have left if we live until 90 years old.

# It will take your current age as the input and output a message with our time left in this format:

# You have x days, y weeks, and z months left.

# Where x, y and z are replaced with the actual calculated numbers.

# 🚨 Don't change the code below 👇
age = input("What is your current age? ")
# 🚨 Don't change the code above 👆

# Write your code below this line 👇

left_age = 90 - int(age)
months_left = left_age * 12
weeks_left = left_age * 52
day_left = left_age * 365

print(
    f"You have {day_left} days, {weeks_left} weeks , and {months_left} months left")
