# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆


# Write your code below this row 👇
totalNum = 0
averageNum = 0

for student in student_heights:
    averageNum += int(student)
    totalNum += 1

averageNum /= totalNum

print(f"The average student height is {round(averageNum)}")

# total_height = sum(student_height)
# number_of_students = len(student_heights)
# average_height = round(total_height / number_of_students)
# print(average_height)
