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


def calculator():
    num1 = int(input("What's the first number?: "))

    for symbol in operation:
        print(symbol)

    operation_symbol = input("Pick an operation form the line above: ")
    num2 = int(input("What's the second number?: "))
    calculation_function = operation[operation_symbol]
    answer = calculation_function(num1, num2)

    print(f"{num1} {operation_symbol} {num2} = {answer}")

    flag = True
    while flag:
        user_respond = input(
            f"Type 'y' to continue calculating with {answer}, or type 'n' to exit:").lower()

        if user_respond == 'y':
            operation_symbol = input("Pick an another operation: ")
            num3 = int(input("What's the next number? "))
            calculation_function = operation[operation_symbol]
            answer = calculation_function(answer, num3)
            print(f"{answer} {operation_symbol} {num3} = {answer}")
        elif user_respond == 'n':
            flag = False
            calculator()
        else:
            continue


calculator()
