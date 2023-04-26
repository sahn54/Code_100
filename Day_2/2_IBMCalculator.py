# Write a program that calculates the Body Mass Index (BMI) from a user's weight and height.

# The BMI is a measure of someone's weight taking into account their height. e.g. If a tall person and a short person both weigh the same amount, the short person is usually more overweight.

# The BMI is calculated by dividing a person's weight (in kg) by the square of their height (in m):


# BMI  = weight (kg) / height^2 (m^2)

weight = int(input("Please enter your weight: "))
height = float(input("Please enter your height: "))
bmi = weight // (height ** 2)

print("Your BMI is :", int(bmi))
