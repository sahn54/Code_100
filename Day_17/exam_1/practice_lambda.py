# what is a lambda function convenient for? something like sorting

student_tuples = [
    ('john', 'A', 15),
    ('adam', 'B', 11),
    ('beth', 'C', 10),
    ('jane', 'A', 3)
]

# the sorted function first of all does not sort in place
# in python, if I call sort() on a list, the list itself is modified
# if I call the sorted() function, the list itself is not modified


def return_second_index(student):
    return student[2]


key_function = return_second_index

sorted_student_tuples_1 = sorted(
    student_tuples, key=lambda student: student[1])
sorted_student_tuples_2 = sorted(student_tuples, key=key_function)
print(sorted_student_tuples_1)
print(sorted_student_tuples_2)
# the sorted function does not affect the original list
a = [5, 2, 4, 9, 1, 0]
b = sorted(a)
print(a)
print(b)

# the sort function sorts in place - the original list a has been modified
a.sort()
print(a)

array_example = [10, 2, 6]

array_example[0] = 0
array_example[-1] = 1
print(array_example)
# print the number of *'s of each element in the list, start at the back of the list
for array_index in range(len(array_example)):
    reverse_index = -1 * (array_index) - 1
    current_element = array_example[reverse_index]
    for x in range(current_element):
        print("*", end="")
    print()

# let's do the same problem also with reverse indexing but with a slightly different strategy
# print the number of *'s of each element in the list, start at the back of the list
for array_index in range(-1, -1 * len(array_example), -1):
    current_element = array_example[array_index]
    for x in range(current_element):
        print("*", end="")
    print()
