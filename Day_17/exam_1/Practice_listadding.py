# def index_add():
#     l = list(range(1, 11))
#     oursum = 0
#     for x in range(0, len(l), 2):
#         oursum += l[x]
#     print(oursum)


# index_add()
import random


# def rand_add():
#     l = []
#     highest = 0
#     for x in range(1, 11):
#         x = random.randint(1, 10)
#         l.append(x)
#         if highest < x:
#             highest = x
#     print(l)
#     print(highest)


# rand_add()

# def max_index():
#     l = []
#     highest = 0
#     highest_index = 0
#     for i in range(1, 11):
#         x = random.randint(1, 10)
#         l.append(x)
#         if highest < x:
#             highest = x
#             highest_index = i
#     print(l)
#     print(highest)
#     print(highest_index)


# max_index()
def max_list(x, i):
    l = []
    for k in range(0, i-1):
        l.append(x[k])
        print(f"{max(l)}, {k}")


a = [4, 2, 7, 1, 45, 23]
max_list(a, 6)
