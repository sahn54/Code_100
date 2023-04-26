# #write a function that takes in a number, and prints each digit that is prime
# #suppose 1 is not prime
# #assume it comes in as an int
# #for example, if the number is 17344 print: 7,3
# #separate by commas, print the higher power of ten first
# from math import sqrt

# #49 if you checked up until 25 you would still get the right answer
# #just like if you checked up until 48 you would also get the right answer
# #what we're doing by taking the square root is optimizing runtime
# #because we know that once we pass the square root, we can't possibly find a value that is a divisor if it has not been found yet

# # 53
# # 2,3,4,5,6,7,8
# # 6 * 8.83 = 53
# # 7 * 7.57 = 53
# # 8 * 6.625 = 53
# # 9 * 6 = 53


# def isprime(number):
#   if number == 1:
#     return False
#   square_root_rounded_up = int(sqrt(number)) + 1
#   for x in range(2,square_root_rounded_up):
#     if number % x == 0:
#       return False
#   return True

# # print(isprime(13))
# # print(isprime(8))

# def print_prime_digits(number):
  
#   #first convert the number to a list where each index has a digit, but only include prime digits as you go
#   #note: getting the digits into a list backwards is the same to us as forwards, because when we traverse it, we can traverse it backwards
#   #17344 -> [3,7]
#   prime_digit_list = []
#   number_copy = number
#   while number_copy > 0:
#     next_digit = number_copy % 10
#     if isprime(next_digit):  
#       prime_digit_list.append(next_digit)
#     number_copy //= 10
  
#   #get the list to be forwards
#   #[3,7] -> [7,3]
#   prime_digit_list_forwards = prime_digit_list[::-1]
#   for prime_digit_index in range(len(prime_digit_list_forwards)):
#     #this line is simply checking whether we are at the last element in the list
#     if prime_digit_index < (len(prime_digit_list_forwards) - 1):
#       print(prime_digit_list_forwards[prime_digit_index], end = ",")
#     else:
#       print(prime_digit_list_forwards[prime_digit_index])

# print_prime_digits(17344)

#write a program using for loops to print the following:

#(1,1) (1,2) (1,3) (1,4)
#(2,1) (2,2) (2,3) (2,4)
#(3,1) (3,2) (3,3) (3,4)
#(4,1) (4,2) (4,3) (4,4)

# indices = [1,2,3,4]

# for row_index in indices:
#   for column_index in indices:
#     print(f"({row_index},{column_index})", end = " ")
#     # final_string_to_print = "(" + str(row_index) + "," + str(column_index) + ")"
#     # print(final_string_to_print, end = " ")
#   print()

# #another way of doing f-strings
# name = "bob"
# age = "20"
# print("Hello, {}. You are {}.".format(name, age))

# print("HELLO","HOW","ARE","YOU", sep = "/", end = "*\n")

# example_string = "HELLO HOW ARE YOU"
# example_list = example_string.split()
# print(example_list)


# x = 10
# x = x + 5
# answer: x = 15

# in python, immutable objects (like tuple, string, and integer) are pass by value essentially, because you are passing the reference, but when you change the number, you only change the pointer of the local variable, so it is effectively pass by value
# mutable objects are pass by reference, so if you pass in a list and modify something in the list, the list itself will change when you return from the function

# list indexing and string indexing (and other kinds of data types we have not seen yet) are done as closely as possible on purpose as ease of use to the programmer

# my_list = [1,2,3]
# reverse_list = my_list[::-1]

# my_string = "123"
# reverse_string = my_string[::-1]

# if you know how to do string indexing, you know how to do list indexing and vice versa


#what is a palindrome? it is a word that is equal to its reverse
#racecar = palindrome
#cart = not palindrome
# def ispalindrome(my_string):
#   return my_string == my_string[::-1]

# print(ispalindrome("racecar"))
# print(ispalindrome("speeps"))
# print(ispalindrome("racecat"))

# a = [0,1,2,3,4,5]
#print(a[2])

# #take in a four-digit integer, return true if palindrome, false if not
# def is_palindrome_four_digit(four_digit_int):
#   #if a four digit number is a palindrome, what does that actually look like?
#   # 2442, 8118, 0990, 1331
#   dig_1 = four_digit_int % 10
#   four_digit_int //= 10
  
#   dig_2 = four_digit_int % 10
#   four_digit_int //= 10

#   dig_3 = four_digit_int % 10
#   four_digit_int //= 10

#   dig_4 = four_digit_int % 10
#   four_digit_int //= 10

#   if dig_1 == dig_4 and dig_2 == dig_3:
#     return True
#   else:
#     return False

# print(is_palindrome_four_digit(1881))
# print(is_palindrome_four_digit(1003))

#to make a more general version of this that can tell you if any number is a palindrome regardless of length,
#we would want to combine the two functions above

# #assume you have a function ispalindrome() which tells you if a string is a palindrome or not. 
# def ispalindrome(my_string):
#   #let's iterate through and check the first character against the last character, the second against the second-to-last, etc until we hit the middle
#   stopping_point = len(my_string) // 2
#   #if the string is seven characters long, suppose racecar
#   #we can stop when we hit the third character (check 0, 1, 2 against 6,5,4 respectively. 3 == 3 automatically)
#   #if the string is six characters long, suppose speeps
#   #we can stop when we hit the third character (check 0,1,2 against 5,4,3 respectively)
#   for x in range(stopping_point):
#     char_1 = my_string[x]
#     char_2 = my_string[(-1 * x) - 1]
#     if char_1 != char_2:
#       return False
#   return True

# #write a function that takes in any size integer and prints to the user whether or not it is a palindrome
# # def is_integer_palindrome(number):
# #   return ispalindrome(str(number))

# def is_integer_palindrome(number):
#   number_string = ""
#   while number > 0:
#     next_digit = number % 10
#     number //= 10
#     number_string = str(next_digit) + number_string
#   return ispalindrome(number_string)

# # print(is_integer_palindrome(100001))
# # print(is_integer_palindrome(232))
# print(is_integer_palindrome(123456))


# given a square matrix, return the value of the diagonals summed up and multiplied with each other
# 1 2 3
# 4 5 6
# 7 8 9

#return (1 + 5 + 9) * (3 + 5 + 7) = 225

def product_of_diagonal_sum(square_matrix):
  number_of_rows = len(square_matrix)
  number_of_cols = len(square_matrix[0])
  
  main_diagonal_sum = 0
  #in this case 1 + 5 + 9
  
  weak_diagonal_sum = 0
  #in this case 3 + 5 + 6

  for r in range(number_of_rows):
    for c in range(number_of_cols):
      if r == c:
        main_diagonal_sum += square_matrix[r][c]
      
      #for the weak diagonal, I want to add to it when r = 0 c = total_columns - 1, r = 1 c = total_columns - 2, etc
      if r + c == number_of_rows - 1:
        weak_diagonal_sum += square_matrix[r][c]
  
  return main_diagonal_sum * weak_diagonal_sum

a = [[1,2,3],[4,5,6],[7,8,9]]
print(product_of_diagonal_sum(a))


