def sum_of_digits(number):
    total_sum = 0

    # for x in range(number): #this loop would run 1729 times which is NOT what we want

    # do it with a while loop
    while number > 0:
        current_digit = number % 10
        # current_digit = 9
        # current_digit = 2
        # last pass through
        # curent_digit = 1
        number //= 10
        # number = 172
        # number = 17
        # number = 0
        total_sum += current_digit
        # total_sum = 9
        # total_sum = 11
        # total_sum = 18
        # total_sum = 19

    return total_sum

# def reverse_digits(regular_number):
#   """
#   if the input is 1729, the output is 9271
#   """
#   reversed_number = 0

#   #do it with a while loop
#   while regular_number > 0:
#     current_digit = regular_number % 10
#     regular_number //= 10

#     #what we want to do is take a number, let's say 92, and add the current_digit to to the front of it. so 92 with current_digit = 7 should give us 927
#     reversed_number *= 10
#     #this would turn 92 -> 920
#     reversed_number += current_digit
#     #this would turn 920 -> 927
#   return reversed_number

# def reverse_string(regular_string):

#   # remember, anythign we can do with a list we can do with a string
#   # also remember, anytime you see the :: with a list or string you know that it is short for start_index (inclusive), end_index (non-inclusive), step (how much to increment by as you move through)
#   # if you leave start_index blank it starts at 0, if you leave end_idnex blank it ends at length of string/list, if you leave step blank it does 1 automatically
#   # I will explain this later
#   # reversed_string = regular_string[::-1]

#   # another way of doing it
#   reversed_string = ""
#   for character in regular_string:
#     # every time I see the next letter in the reversed_string, add it to the FRONT of the reversed_string
#     # the first letter I see is gonna end up all the way in the back
#     reversed_string = character + reversed_string


#   return reversed_string


# # x = sum_of_digits(1729)
# # y = reverse_digits(1729)
# z = reverse_string("hello")
# print(z)

# def binary_conversion(decimal_number):
#   binary_string = ""
#   while decimal_number > 0:

#     new_digit = decimal_number % 2 # this will either equal 0 or 1, depending on this version of decimal_number is odd or even

#     #one way of doing it
#     binary_string = str(new_digit) + binary_string

#     # #another way of doing it
#     # if new_digit == 0:
#     #   binary_string = '0' + binary_string
#     # #the only other option is that it equals 1
#     # else:
#     #   binary_string = '1' + binary_string

#     decimal_number //= 2
#   return binary_string

# def binary_to_decimal(binary_string):
#   decimal_number = 0
#   current_power_of_2 = 0
#   #going in reverse order. so if we see 100 as the binary_string, it will iterate through '0', then '0', then '1'
#   for binary_digit in binary_string[::-1]:
#    decimal_number = decimal_number + int(binary_digit) * (2 ** current_power_of_2)
#    current_power_of_2 += 1

#   return decimal_number


# bin_string = binary_conversion(1729)
# print(bin_string)
# dec_number = binary_to_decimal(bin_string)
# print(dec_number)

# 145 -> 5 * 10^0 + 4 * 10^1 + 1 * 10^2

# 1001 -> 1 * 2^0 + 0 * 2^1 + 0 * 2^2 + 1 * 2^3 = 9

# 9
# 9 % 2 -> = 1 (new_digit)
# 9 / 2 = 4 (new_number)

# 1

# 4 % 2 -> 0 (new_digit)
# 4 / 2 -> 2 (new_number)
# 01 (build the binary number by putting the new_digit in the front of the old binary number so 1 with new digit 0 becomes 01)

# 2 % 2 = 0 (new_digit)
# 2 / 2 = 1
# 001

# 1001

# one way of doing it
# def is_palindrome(our_string):
#   reversed_string = ""
#   for character in our_string:
#     reversed_string = character + reversed_string
#   if reversed_string == our_string:
#     return True
#   else:
#     return False

# def is_palindrome(our_string):
#   reversed_string = our_string[::-1]
#   if reversed_string == our_string:
#     return True
#   else:
#     return False

def is_palindrome(our_string):
    # build this without using an additional string

    # there are two palindromes. there are those with even number of characters and odd
    length_of_palindrome = len(our_string)
    midpoint = length_of_palindrome // 2
    # range(midpoint) is not including midpoint, like we know about the range function
    # here it does not matter, because we don't need to check the midpoint in either an even letter palindrome or odd case
    # for the odd case, the middle letter must equal itself. suppose length 7, midpoint = 7 // 2 = 3. if we check index 0 through 2 against index 6 through 4, index 3 must equal index 3
    # for the even case, suppose length 4, 4 // 2 = 2. in this case, we will check all letters because we wil lcheck index 0 against 3, 2 against 1, and then midpoint equals 2 and we stop
    # if the string is
    for index_from_start in range(midpoint):
        # the reason why we did length_of_palindrome - 1 - index_from_start as our index is because
        # had we not, the first time we check the index
        # suppose the string was "coloc"
        # we would be checking the 0 index "c" against the length - index_from_start (had we not done -1)
        # the length is 5, the index_from_start is 0 (because that is the first iteration)
        # so we would be checking the fifth index which is out of range
        if our_string[index_from_start] != our_string[length_of_palindrome - 1 - index_from_start]:
            return False

    return True


print(is_palindrome("kook"))
print(is_palindrome("raceca"))

# string_1 = "test"
# string_2 = "test"
# string_1 == string_2 THIS WILL RETURN FALSE IN JAVA
# because Java compares memory addresses for objects, and a string is an object
# in java, you have to call string_1.equals(string_2) to compare the values

# in python
# string_1 = "test"
# string_2 = "test"
# string_1 and string_2 are pointing to the same location of memory
