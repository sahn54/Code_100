# b - a
# b
# C
# a
# b
# a
# a
# a
# b

matrix = [[1, 2], [3, 4]]
transposed = [[row[i] for row in matrix] for i in range(len(matrix[0]))]
print(transposed)
