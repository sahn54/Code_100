
with open("Code_100/Day_26/file1.txt") as file_1:
    file_container_1 = file_1.readlines()

with open("Code_100/Day_26/file2.txt") as file_2:
    file_container_2 = file_2.readlines()
result = [int(file_container_1[num])
          for num in range(0, len(file_container_1)) if file_container_1[num] in file_container_2]

result = [int(num)
          for num in file_container_1 if num in file_container_2]


# Write your code above 👆

print(result)
