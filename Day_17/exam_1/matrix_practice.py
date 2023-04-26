# 1 2 3
# 4 5 6
# 7 8 9

# return (1 + 5 + 9) * (3 + 5 + 7) = 225


def product_of_diagonal_sum(Sqr_matix):
    num_row = len(Sqr_matix)
    num_col = len(Sqr_matix[0])
    main_diagonal_sum = 0
    # 1 + 5 + 9
    weak_diagonal_sum = 0
    # 3 + 5 + 7
    for r in range(num_row):
        for c in range(num_col):
            if r == c:
                main_diagonal_sum += Sqr_matix[r][c]
            if r + c == num_row - 1:
                weak_diagonal_sum += Sqr_matix[r][c]
    return main_diagonal_sum * weak_diagonal_sum


a = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(product_of_diagonal_sum(a))
