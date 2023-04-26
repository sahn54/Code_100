# Write a Python function to calculate the factorial of a number.
def my_factorial(num):
    final_num = 1
    for i in range(1, num + 1):
        final_num *= i
    return final_num


myNumber = my_factorial(4)
print(f"Factorial: {myNumber}")


# Write a Python program to print the first 10 Fibonacci numbers.
def fibonacci(num2):
    a = 0
    b = 1
    result = 0
    for i in range(num2+1):
        if i < 1:
            print(result, end=" ")
            result += b
        else:
            print(result, end=" ")
            result = a + b
            a = b
            b = result
    return ""


print(fibonacci(20))


# Write a Python function to check whether a string is a palindrome or not.
def ispalindrome(s):
    return s == s[::-1]


status = ispalindrome("level")
if status == True:
    print("The string is a palindrome ")
else:
    print("The string is not palindrome")

# Write a Python program to find the largest element in a list.


def largest(our_list):
    largest_num = 0
    for i in our_list:
        if largest_num < i:
            largest_num = i
    return largest_num


k_list = [345, 667, 31, 321, 55, 6666, 7889, 3, 14, 45]

print(largest(our_list=k_list))
# Write a Python program to count the number of vowels in a string.


def vowels(our_String):
    vowelsList = ['a', 'e', 'i', 'o', 'u']
    count = 0
    for i in our_String:
        if i in vowelsList:
            count += 1
    return count


print(vowels("prime"))


# Write a Python function to check whether a number is prime or not.
def checkPrime(p):
    isPrime = False
    if p == 1:
        return isPrime
    elif p > 1:
        for i in (2, p):
            if (p % i) == 0:
                isPrime = True
                break
    return isPrime


print(checkPrime(29))

# Write a Python program to sort a list of numbers in ascending order.


def sortList(l_List):
    for i in range(len(l_List)):
        for j in range(i+1, len(l_List)):
            if l_List[i] > l_List[j]:
                l_List[i], l_List[j] = l_List[j], l_List[i]
    return l_List


print(sortList(l_List=k_list))


# Write a Python program to reverse a string.


def reverseString(s):
    return s[::-1]


print(reverseString("Hello World"))

# Write a Python function to calculate the area of a triangle given its base and height.


def triangleCalculate(base, height):

    area = base * height * (1/2)

    return int(area)


print(triangleCalculate(13, 26))

# Write a Python program to remove all duplicates from a list.


def removeDuplicates(theList):
    noDuplicates = set()
    finalList = []
    for i in theList:
        if i not in noDuplicates:
            finalList.append(i)
            noDuplicates.add(i)

    return finalList


j_list = [23, 3, 4, 5, 6, 2, 1, 1, 22, 33, 2, 21, 56, 1, 32]


print(removeDuplicates(theList=j_list))
