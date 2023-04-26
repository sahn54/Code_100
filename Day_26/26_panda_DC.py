# Using Panda for dictionary comprehension

import pandas
student_dict = {
    "student": ["Sung", "James", "Lily"],
    "score": [56, 76, 98]
}

# Looping through dictionaries:
# for (key, value) in student_dict.items():
#     print(value)

# Looping names
student_data_frame = pandas.DataFrame(student_dict)
print(student_data_frame)

# Loop through a data frame getting values
# for (key, value) in student_data_frame.items():
#     print(value)


# loop through rows of a data frame
for (index, row) in student_data_frame.iterrows():
    if row.student == "Sung":  # type: ignore
        print(row.score)  # type: ignore
