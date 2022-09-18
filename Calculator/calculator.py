from art import logo

def add(n1, n2):
    return n1+n2

def subtract(n1, n2):
    return n1-n2


def multiply(n1, n2):
    return n1 * n2


def divide(n1, n2):
    return n1/n2

def calculator():
    print(logo)
    operations = {
        "+": add,
        "-": subtract,
        "*": multiply,
        "/": divide
    }

    num1 = float(input("What's the first number? "))

    for i in operations:
        print(i)

    shouldContinue = True

    while shouldContinue:

        operationSelected = input("Select an operation: ")
        num2 = float(input("What's the next number? "))
        function = operations[operationSelected]
        answer = function(num1, num2)

        print(f"{num1} {operationSelected} {num2} = {answer}")

        if input(f"type'y' to continue calculating with {answer}, or type 'n' to start a new calculation.: ") == "y":
            num1 = answer
        else:
            shouldContinue = False
            calculator()

calculator()