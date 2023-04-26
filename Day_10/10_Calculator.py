def add(n1, n2):
    return n1 + n2


def subtract(n1, n2):
    return n1 - n2


def multiply(n1, n2):
    return n1 * n2


def divide(n1, n2):
    return n1 / n2


operation = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide

}


num1 = int(input("What's the first number?: "))


for symbol in operation:
    print(symbol)

operation_symbol = input("Pick an operation form the line above: ")
num2 = int(input("What's the second number?: "))
calculation_function = operation[operation_symbol]
answer = calculation_function(num1, num2)
print(f"{num1} {operation_symbol} {num2} = {answer}")
