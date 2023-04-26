def even_indices(matrix):
    even_element = []
    for r_index in range(len(matrix)):
        if r_index % 2 == 0:
            even_element.append(matrix[r_index][r_index])
    return even_element


m = [[1, 2, 3, 4], [2, 3, 3, 3], [7, 8, 9, 6], [3, 4, 6, 7]]

print(even_indices(m))
