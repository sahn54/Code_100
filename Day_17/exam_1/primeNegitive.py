# PRACTICE AND WE'LL SOLVE THE NEXT TIME:
# write a function that takes in a number, and prints each digit that is prime
# suppose 1 is not prime
# assume it comes in as an int
# for example, if the number is 17344 print: 7,3
# separate by commas, print the higher power of ten first
# def takeout_prime_String(num, sep=","):
#     def isPrime(i):
#         if i < 2:
#             return False
#         for j in range(2, int(i**0.5)+1):
#             if i % j == 0:
#                 return False
#         return True
#     prime_numbers = ""
#     first_Prime = True
#     for n in num:
#         if isPrime(int(n)):
#             if not first_Prime:
#                 prime_numbers += sep
#             prime_numbers += n
#             first_Prime = False
#     return prime_numbers


# print(takeout_prime_String("123456789"))


def isPrime(i):
    if i < 2:
        return False
    for j in range(2, int(i**0.5)+1):
        if i % j == 0:
            return False
    return True


def takeout_prime_int(num, sep=","):

    prime_numbers = []
    numcopy = num
    while numcopy > 0:
        numcopy = num % 10
        numcopy //= 10


print(takeout_prime_int(123456789))

# def takeout_prime_int(num, sep=","):
#     primes = []
#     for n in range(2, num+1):
#         is_prime = True
#         for i in range(2, int(n**0.5)+1):
#             if n % i == 0:
#                 is_prime = False
#                 break
#         if is_prime:
#             primes.append(str(n))
#     return sep.join(primes)


# print(takeout_prime_int(123456789))


# 1. Check if the number is less than 2. If it is less than 2, it is not prime.

# 2. If the number is 2, it is prime.

# 3. If the number is even (other than 2), it is not prime because it is divisible by 2.

# 4. If the number is odd, we can check whether it is divisible by any odd number from 3 up to the square root of the number. If it is not divisible by any of these numbers, then it is prime.


# def check_Prime(n):
#     if n < 2:
#         return False
#     if n == 2:
#         return True
#     if n % 2 == 0:
#         return False
#     for i in range(3, int(n**0.5) + 1, 2):
#         if n % i == 0:
#             return False
#     return True


# l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]

# for n in l:
#     if check_Prime(n):
#         print(n, "is prime")
#     else:
#         print(n, "is not prime")
