sum = 0
for num in range(1, 101):
    if num % 2 == 0:
        sum += num
print(sum)

# or

total = 0
for number in range(2, 101, 2):
    total += number
print(total)
