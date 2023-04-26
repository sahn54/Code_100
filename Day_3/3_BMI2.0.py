# BMI  = weight (kg) / height^2 (m^2)

weight = int(input("Please enter your weight: "))
height = float(input("Please enter your height: "))
bmi = round(weight / height ** 2)

if bmi <= 18.5:
    print(f"Your BMI is : {bmi} You are underweight")
elif bmi < 25:
    print(f"Your BMI is : {bmi} You are normal weight")
elif bmi < 30:
    print(f"Your BMI is : {bmi} You are slightly overweight")
elif bmi < 35:
    print(f"Your BMI is : {bmi} You are obese.")
else:
    print(f"Your BMI is : {bmi} You are clinically obese.")
