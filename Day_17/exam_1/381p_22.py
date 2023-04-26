# def isprime(number):
#   # a prime number is a number for which the only factors are 1 and itself
#   # for example, 19 is a prime number because the only numbers that "go into" 19 are 1 and 19
#   if number <= 2:
#     return True

#   for x in range(2, int(number**.5)+1):

#     #this line is basically trying to find factors x that fit into the number we are examining
#     if number % x == 0:
#       return False

#   return True


# print(isprime(13))
# print(isprime(8))

# 973 is this number prime?
# intuition: if you want to find the answer the long way,
# you know you can stop looking once you hit 487
# because at that point, any number higher would have to multiply by a number less than 2

# more powerful intuition:
# 17 is this number prime?
# once I pass 5, I don't have to check anything anymore
# we're searching for an integer x that when multiplied by an integer y gives us 17
# x * y = 17
# 2 * y = 17 NO (y = 8.5)
# 3 * y = 17 NO (y = 5.67)
# 4 * y = 17 NO (y = 4.25)
# 5 * y = 17 NO (y = 3.67)

# a problem with *args
# use *args for a variable number of arguments
# def our_sum(a, *waxman):
#   result = 0
#   for x in waxman:
#     result += x
#   return (a * result)

# def our_product(*args):
#   product = 1
#   for x in args:
#     product *= x
#   return product


# a = our_sum(10,1,2,3,4,5)
# b = our_product(1,2,3,4,5)
# print(a)
# print(b)


# matrix question
# given a matrix of positive integers, and given an integer x by the user, find the maximum value in the square matrix.
# if the maximum value is not greater than the number x given by the user, return the number 20. otherwise, return the maximum

# def find_max_return_twenty(square_matrix, x):
#   rows = len(square_matrix)
#   cols = len(square_matrix[0])
#   maximum = 0
#   for r in range(rows):
#     for c in range(cols):

#       #if I found a new maximum, reset maximum to that value
#       if square_matrix[r][c] > maximum:
#         maximum = square_matrix[r][c]

#   if maximum <= x:
#     return 20
#   else:
#     return maximum

# square_matrix_one = [[1,2,3],[8,12,1]]
# print(find_max_return_twenty(square_matrix_one, 13))

# square_matrix_two = [[1,2,3],[8,12,1],[30,1,0],[10,1,25]]
# print(find_max_return_twenty(square_matrix_two, 25))

# # lambda expression
# a = lambda x , y, z: max(x,y,z)
# print(a)
# r = a(3,4,5)
# print(r)

# list comprehension
# generate a list with all numbers that end in a 9 between 0 and 1000
# use list comprehension
# solution_list = []
# for x in range(1000):
#   if x % 10 == 9:
#     solution_list.append(x)

# solution_list = [x for x in range(1000) if x % 10 == 9]

# x = [0,1,2]
# y = [3,4,5]
# dot_product_helper_list = [y[index] * x[index] for index in range(len(x))]
# print(dot_product_helper_list)
# dot_product = sum(dot_product_helper_list)
# print(dot_product)

# print(solution_list)


# SORTING (OLD CODE)
# stable sort what it is
# the elements that are the same that come in a certain order need to stay in that order
# [Judge, Alonso, Trout, Harper]
# Judge:37, Alonso: 40, Trout: 37, Harper:43
# sort from most HRs to least HRs
# both of the following are valid
# Harper, Alonso, Trout, Judge
# STABLE SORT GUARANTEES: Harper, Alonso, Judge, Trout
# a stable sort would be able to guarantee: Harper, Alonso, Judge, Trout (every single time)
# a stable sort is a sort that guarantees that for elements with the same key value, the order they enter with is the order they exit with

# seniority used as a tie-breaker, guaranteed

# try coding insertion sort

# for (int j = 10; j >= 0; j--) {
# for (int j = 10; j > -1; j--) {

# def insertion_sort(number_array):
#   correctly_placed_numbers = 0
#   for number_to_place in number_array:

#     # we go until -1 because we want to include going through the zero index, for when we hit the front of the array
#     # python does not execute the loop for the end_index. in this case, that's -1. but it will execute everything until then, which means in our case, it will execute 0 which is what we want
#     for index_of_previously_seen_number in range(correctly_placed_numbers, -1, -1):

#       #check if we hit the beginning of the list, in which case place the element
#       if index_of_previously_seen_number == 0:
#         number_array[0] = number_to_place
#         break

#       #when we run this, suppose element 0 = 5, element 1 = 2
#       #correctly_placed_numbers = 1, so the first index we are gonna look at is 1
#       #that is actually where 2 is already located!
#       #but the reason we're doing that is that if we do not, then when 2 is examined, we will already be at index 0
#       #the if loop above will execute, and we will "lose" 5 and never actually place it
#       #since we want to move 5 first, we are gonna start at index 1, where 2 is currently located, to give us room to move 5 into

#       previously_seen_number = number_array[index_of_previously_seen_number - 1]

#       #stable sort: insertion sort is stable, because this is < and it is not <=
#       #this is the key component that makes it a stable sort!
#       if number_to_place < previously_seen_number:

#         #move the previously_seen_number over by one to create space for the new number
#         number_array[index_of_previously_seen_number] = previously_seen_number
#         #this connects to the huge comment thing above
#         #we are placing 5 where we are RIGHT NOW when we are looking at 2 - which is index 1, where 2 is currently located
#       else:

#         #place the number_to_compare in the current index
#         number_array[index_of_previously_seen_number] = number_to_place
#         break

#     correctly_placed_numbers += 1

#   return number_array


# for (int i = 10; i >= 0; i--)
# all python lets you do
# for (int i = 10; i > -1; i--)


# number_array = [2,5,7,4,7,13,1,8]
# print(insertion_sort(number_array))

# from random import randint

# fill up a 2D matrix of random numbers between 1-100 using list comprehensions
# def return_2d_matrix(rows, cols):
#   return [[randint(1,101) for c in range(cols)] for r in range(rows)]

# def return_2d_matrix(rows, cols):
#   two_d_matrix = []
#   for r in range(rows):
#     two_d_matrix.append([randint(1,101) for c in range(cols)])
#   return two_d_matrix


# a = return_2d_matrix(4,7)
# print(a)


# OLD CODE
import random

# ask the user for three integer n, m, k where k > (m*n)
# create a two dimensional table (list of lists) x of size n*m
# populate the list with n*m unique random integers in the range 1 through k

# 3 x 4 array
# 3 rows, 4 columns
# a[r][c]

# a[1][2]

# row 0 (array 0): 1, 2, 3, 4
# row 1 (array 1): 1, 2, 3, 4
# row 2 (array 2): 1, 2, 3, 4


# in this problem
# final answer is gonna be n rows, m columns
# answer_array
# answer_array[row][column] =

def two_dimensional_randoms():
    n = int(input("enter n: "))
    m = int(input("enter m: "))
    k = int(input("enter k: "))
    if k <= (m*n):
        print("You have not entered numbers that meet the requirements")
        return

    already_used_numbers = set()
    # technically one-dimensional right now, but we can add lists inside of it
    two_dimensional_solution = []
    # if I add three lists to this [[1,2,3],[2,3,4],[3,4,5]]
    # by default starts at 0, goes until but not including END_INDEX

    # loop through all of the rows, one iteration per row
    for x in range(n):

        # all the numbers we have so far in the current iteration for the row. clear at the start of the row
        current_row_numbers = []

        # loop through as many columns as specified
        for y in range(m):

            # we need the number to be unique. start off by assuming it's not unique to just make sure the while loop runs at least once
            number_unique = False

            # keep searching until we get a unique number
            while number_unique is False:

                # generate a random number on the specified interval
                random_number = random.randint(1, k)

                # only allow the program to continue and add the new number if it is not already used
                if random_number not in already_used_numbers:
                    number_unique = True

                    # add the number we find to the set
                    already_used_numbers.add(random_number)

            # once we find a unique number, add it to the current_row_numbers
                current_row_numbers.append(random_number)
            # looking inside current_row_numbers
            # after the first iteration [17]
            # then [17,34]
            # etc until you finish going through all the columns

        # when a full row is finished, add it to the two_dimensional_solution
        two_dimensional_solution.append(current_row_numbers)
        # what this will look like as it grows:
        # it will start off empty []
        # [[17,34]] [] -> add to that list [17,34] which is being considered to an element
        # on the second iteration
        # [[17,34],[18,22]] -> add to the list [18,22]
        # etc until you finish filling up all the rows

    print(two_dimensional_solution)
