import sys

class InputException(Exception):
    pass

def inputNumber():
    num = ""
    while not num.replace(".", "", 1).isdigit():
        try:
            num = input("Enter the digit (ex. 1 or 1.5): ")
            if num == "exit":
                print("Exiting the program")
                sys.exit(1)
            elif not num.replace(".", "", 1).isdigit():
                raise InputException("EXCEPTION: NOT A DIGIT")
        except InputException as error:
            print(error)
    return num

def inputOperator():
    operator = ""
    while operator not in ("+", "-", "/", "*", "sqrt", "^", "%"):
        try:
            operator = input("Enter the operator (+, -, /, *, sqrt, ^, %): ")
            if operator == "exit":
                print("Exiting the program")
                sys.exit(1)
            elif operator not in ("+", "-", "/", "*", "sqrt", "^", "%"):
                raise InputException("EXCEPTION: OPERATOR CAN ONLY BE +, -, /, *, sqrt, ^, or %")
            elif operator == "sqrt":
                num2 = None
                return
        except InputException as error:
            print(error)
    return operator