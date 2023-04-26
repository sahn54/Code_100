def pyrimid():
    # for x in range(9):
    #     print(" "*x, end="")
    #     for i in range(1+x, 10):
    #         print(i, end="")
    #     for i in range(8, 0+x, -1):
    #         print(i, end="")
    #     print()
    for x in range(8, -1, -1):
        print(" "*x, end="")
        for i in range(1+x, 10):
            print(i, end="")
        for i in range(8, 0+x, - 1):
            print(i, end="")
        print()


pyrimid()
