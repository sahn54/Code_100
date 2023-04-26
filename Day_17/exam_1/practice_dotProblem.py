# the dot product question
x = [1, 2, 3]
y = [5, 6, 10]
# we want the dot product = x0y0 + x1y1 + x2y2 = 1*5 + 2*6 + 3 * 10 = 47

dot_product_sum = 0
# this for loop will iterate through 0, then 1, then 2, and stop because range function is not inclusive and since length = 3, it will NOT run for index_position = 3
for index_position in range(len(x)):
    dot_product_sum += x[index_position] * y[index_position]
print(dot_product_sum)

# let's do the problem the long way the same way we did list comprehension
# that way we'll be able to see the exact conversion from long-form to list comprehension
dot_product_sum = 0
dot_product = []
# this for loop will iterate through 0, then 1, then 2, and stop because range function is not inclusive and since length = 3, it will NOT run for index_position = 3
for index_position in range(len(x)):
    dot_product.append(x[index_position] * y[index_position])
dot_product_sum = sum(dot_product)
print(dot_product_sum)

# now let's do this problem as a list comprehension
# first we want to make a list where each index is equal to the x_index * y_index for that index
# for example, we want the 0 index of our solution "dot_product" to equal x0*y0 = 1*5 = 5
dot_product = [x[index_position] * y[index_position]
               for index_position in range(len(x))]
dot_product_sum = sum(dot_product)
print(dot_product_sum)
