logo = """
 _____________________
|  _________________  |
| | Pythonista   0. | |  .----------------.  .----------------.  .----------------.  .----------------. 
| |_________________| | | .--------------. || .--------------. || .--------------. || .--------------. |
|  ___ ___ ___   ___  | | |     ______   | || |      __      | || |   _____      | || |     ______   | |
| | 7 | 8 | 9 | | + | | | |   .' ___  |  | || |     /  \     | || |  |_   _|     | || |   .' ___  |  | |
| |___|___|___| |___| | | |  / .'   \_|  | || |    / /\ \    | || |    | |       | || |  / .'   \_|  | |
| | 4 | 5 | 6 | | - | | | |  | |         | || |   / ____ \   | || |    | |   _   | || |  | |         | |
| |___|___|___| |___| | | |  \ `.___.'\  | || | _/ /    \ \_ | || |   _| |__/ |  | || |  \ `.___.'\  | |
| | 1 | 2 | 3 | | x | | | |   `._____.'  | || ||____|  |____|| || |  |________|  | || |   `._____.'  | |
| |___|___|___| |___| | | |              | || |              | || |              | || |              | |
| | . | 0 | = | | / | | | '--------------' || '--------------' || '--------------' || '--------------' |
| |___|___|___| |___| |  '----------------'  '----------------'  '----------------'  '----------------' 
|_____________________|
"""

print(logo)


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


def calculate_result(num1, num2, opr):
    return available_operations[opr](num1, num2)


first_num = int(input("What's the first number?: "))

while True:
    print("+\n-\n*\n/")
    operation = input("Pick an operation: ")

    second_num = int(input("What's the second number?: "))

    result = calculate_result(first_num, second_num, operation)

    print(f"{first_num} {operation} {second_num} = {result}")

    continue_current = (False, True)[
        input(
            f"Type 'y' to continue calculating with {result}, or type 'n' to start a new calculation: ").lower() == "y"]
    
    if continue_current:
        first_num = result
    else:
        print("\n" * 20)
        first_num = int(input("What's the first number?: "))
