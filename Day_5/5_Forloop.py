# # For Loops with Lists
# fruit_box = ["Apple", "Peach", "Pear"]

# for fruit in fruit_box:
#     print(fruit)
#     print(fruit, "Pie")
# print(fruit_box)

# # For Loops with range
# for number in range(1, 10):
#     print(number)  # not includes 10
# print("-------------------------------")
# for number2 in range(1, 11, 3):
#     print(number2)  # =+ 3
# print("-------------------------------")
# total = 0
# for number3 in range(1, 101):
#     total += number3
# print(total)


# the sum of all prime number from 1 to 100
sum = 0

for isPrime in range(2, 101):
    for j in range(2, isPrime):
        if isPrime % j == 0:
            break
    else:
        sum += isPrime

print(sum)
