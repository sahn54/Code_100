import random
even_numbers_zero_through_hundred = []
for number in range(101):
    if number % 2 == 0:
        even_numbers_zero_through_hundred.append(number)

# for list comprehension: expression you want to add to the list, for loop, if condition

even_numbers_zero_through_hundred = [
    number for number in range(101) if number % 2 == 0]

print(even_numbers_zero_through_hundred)


# Write a list comprehension that takes a list of strings and returns a new list containing the length of each string in the original list.
my_list = ['my', 'dog', 'king', 'dom', 'jack']


# def len_str(k):
#     new_list = []
#     for i in k:
#         new_list.append(len(i))
#     print(new_list)

def len_str(k):
    new_list = [len(i) for i in k]
    print(new_list)


len_str(k=my_list)


# Given a list of integers, write a list comprehension that returns a new list containing only the even integers from the original list.


def new_numlist(l):

    # new_list2 = []
    # for i in l:
    #     if i % 2 == 0:
    #         new_list2.append(i)
    # print(new_list2)

    new_list2 = [i for i in range(1, len(l)) if i % 2 == 0]
    print(new_list2)


num_list = [1, 2, 3, 4, 5]
new_numlist(l=num_list)
# Given a list of strings, write a list comprehension that returns a new list containing only the strings that start with a vowel (i.e., 'a', 'e', 'i', 'o', or 'u').

# Given two lists of integers of the same length, write a list comprehension that returns a new list containing the sum of the corresponding elements of the two lists. For example, if the input lists are [1, 2, 3] and [4, 5, 6], the output list should be [5, 7, 9].

# Given a list of words, write a list comprehension that returns a new list containing only the words that have more than five letters and start with a capital letter.


def list_num(n, m):
    new_list = []
    my_set = set()

    unique = False
    for i in range(1, n):
        k = random.randint(1, m)
        if k not in my_set:
            unique = True
            my_set.add(k)
            new_list.append(k)

    print(new_list)


list_num(14, 13
         )
