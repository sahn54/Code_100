# Dictionary Comprehension

# new_dict = {new_key:new_value for (key,value) in dict.items() if test}

# example:
import random
names = ["Alex", "Beth", "Caroline", "Dave", "Elanor", "Freddie"]
students_scores = {student: random.randint(1, 100) for student in names}

passed_students = {student: grade for (
    student, grade) in students_scores.items() if grade >= 60}

print(students_scores)
print(passed_students)
