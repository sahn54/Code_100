def isplaindrome(my_string):
    return my_string == my_string[::-1]


def is_int_plaindrome(number):
    return isplaindrome(str(number))


print(is_int_plaindrome(123456))
print(is_int_plaindrome(1001))
