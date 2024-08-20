import art

print(art.logo)


def add(num1, num2):
    """Add 2 numbers"""
    return num1 + num2


def subtract(num1, num2):
    """Subtract 2 numbers"""
    return num1 - num2


def multiply(num1, num2):
    return num1 * num2


def divide(num1, num2):
    return num1 / num2


available_operations = {
    "+": add,
    # You can store a function's name without parenthesis like this and this way, '+ wil be referencing the add function which can be invoked by +(arg1, arg2)
    "-": subtract,
    "*": multiply,
    "/": divide,
}

first_num = float(input("What's the first number?: "))

while True:
    print("+\n-\n*\n/")
    operation = input("Pick an operation: ")

    second_num = float(input("What's the second number?: "))

    result = available_operations[operation](first_num, second_num)

    print(f"{first_num} {operation} {second_num} = {result}")

    continue_current = (False, True)[
        input(
            f"Type 'y' to continue calculating with {result}, or type 'n' to start a new calculation: ").lower() == "y"]

    if continue_current:
        first_num = result
    else:
        print("\n" * 20)
        print(art.logo)
        first_num = float(input("What's the first number?: "))
