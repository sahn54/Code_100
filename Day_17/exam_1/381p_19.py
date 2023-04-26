# write a function that, for a square matrix, returns a list containing all elements whose indices for both the row and column are even and equal
# for example, on a 8x8 matrix, it should return a[0,0],a[2,2],a[4,4],a[6,6] note that a[8,8] would be out of range so we can't return it
# def return_even_indices(square_matrix):
#   # even_and_equal_elements = []
#   # for matrix_index in range(len(square_matrix)):
#   #   if matrix_index % 2 == 0:
#   #     even_and_equal_elements.append(square_matrix[matrix_index][matrix_index])
#   # return even_and_equal_elements

#   #now let's try doing it with list comprehension
#   even_and_equal_elements = [square_matrix[matrix_index][matrix_index] for matrix_index in range(len(square_matrix)) if matrix_index % 2 == 0]
#   return even_and_equal_elements

# a = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
# #a[0,0] = 1
# #a[2,2] = 11
# #solution: [1,11]
# print(return_even_indices(a))


# a = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
# sum_of_all_elements = 0
# for row_index in range(len(a)):
#   length_of_current_row = len(a[row_index])
#   for column_index in range(length_of_current_row):
#     sum_of_all_elements += a[row_index][column_index]
# print(sum_of_all_elements)

# this loop runs nine times, with x values 0 through 8 including 8 but not including 9
for x in range(9):

    # the first time this runs, the line will start with zero blanks. then one blank, then two blanks, etc then 8 blanks
    print(" "*x, end='')

    # the first time this runs, we're gonna start at 1, and print 123456789 and then stop because the range() function is not inclusive of the endpoint at the end
    # the second time this runs, we're gonna start at 2 (since 1 + 1 = 2 and x will equal 1 on the second iteration), so it will print 23456789
    for i in range(1+x, 10):
        print(i, end='')

    # the first this runs, we're gonna start at 8, print 8, then keep going until we hit 0 (but not including zero) so we print 87654321
    # the second time this runs, we're gonna stop one number earlier because we stop at 0+x. so we're gonna print 8765432 the second time through
    for i in range(8, 0+x, -1):
        print(i, end="")

    # print a newline before going to the next iteration
    print()

# in java: for (int i = 0; i < 10; i++)
# in python: for i in range(10)
# these are equivalent

# let's predict what the solution will look like
# let B represent a blank space

# line 0:12345678987654321
# line 1:B234567898765432
# line 2:BB3456789876543
# etc
# line 8:BBBBBBBB9

# line 8 prediction logic:
# for i in range(9,10) only RUNS ONCE for the value i = 9 since start_index is inclusive but end_index is not inclusive
# for i in range(8,8) never runs because it hits the end index right away. it's like having a while loop where the condition starts off false


# a = 3
# b = 4
# c = 5
# print(a,b,c,sep='/',end='*\n')

# d = 8
# print(d, sep="&", end = "***\n")

# THE CODE BELOW IS FROM A PREVIOUS OFFICE HOURS
# import random

# ask the user for three integers n, m, k where k > (m*n)
# create a two dimensional table (list of lists) of size n*m
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

# def two_dimensional_randoms():
#   n = int(input("enter n: "))
#   m = int(input("enter m: "))
#   k = int(input("enter k: "))
#   if k <= (m*n):
#     print("You have not entered numbers that meet the requirements")
#     return

#   already_used_numbers = set()
#   two_dimensional_solution = [] #technically one-dimensional right now, but we can add lists inside of it
#   #if I add three lists to this [[1,2,3],[2,3,4],[3,4,5]]
#   #the range function in general: by default starts at 0, goes up until but not including END_INDEX

#   # loop through all of the rows, one iteration per row
#   for x in range(n):

#     #all the numbers we have so far in the current iteration for the row. clear at the start of the row
#     current_row_numbers = []

#     #loop through as many columns as specified
#     for y in range(m):

#       #we need the number to be unique. start off by assuming it's not unique to just make sure the while loop runs at least once
#       number_unique = False

#       #keep searching until we get a unique number
#       while number_unique is False:

#         #generate a random number on the specified interval
#         random_number = random.randint(1,k)

#         #only allow the program to continue and add the new number if it is not already used
#         if random_number not in already_used_numbers:
#           number_unique = True

#           # add the number we find to the set
#           already_used_numbers.add(random_number)

#       #once we find a unique number, add it to the current_row_numbers
#       current_row_numbers.append(random_number)
#       # looking inside current_row_numbers
#       # after the first iteration [17]
#       # then [17,34]
#       #etc until you finish going through all the columns

#     #when a full row is finished, add it to the two_dimensional_solution
#     two_dimensional_solution.append(current_row_numbers)
#     #what this will look like as it grows:
#     #it will start off empty []
#     # [[17,34]] [] -> add to that list [17,34] which is being considered to an element
#     # on the second iteration
#     #[[17,34],[18,22]] -> add to the list [18,22]
#     #etc until you finish filling up all the rows

#   print(two_dimensional_solution)


# two_dimensional_randoms()

# #NEW PROBLEM: looking at lambda in python
# #lambda is an unnamed function, written quickly as a convenience to the writer
# a = lambda x,y: x + y

# #this line is equivalent to writing things the long way
# # def a(x,y):
# #   return x + y

# #for example, if you wanted a function that can take in two numbers, print as many *'s as the first number, and then as many # symbols as the second number, you can't do that with a lambda
# def a(x,y):
#   print(x * "8")
#   print(y * "#")
#   return

# r = a(2,3)
# print(r)


# PRACTICE AND WE'LL SOLVE THE NEXT TIME:
# write a function that takes in a number, and prints each digit that is prime
# suppose 1 is not prime
# assume it comes in as an int
# for example, if the number is 17344 print: 7,3
# separate by commas, print the higher power of ten first
