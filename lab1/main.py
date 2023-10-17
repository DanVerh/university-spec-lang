import sys
import math

class GeneralException(Exception):
    pass

def inputData():
    global num1, operator, num2

    try:
        num1 = input("Enter the first digit (ex. 1 or 1.5): ")
        if not num1.replace(".", "", 1).isdigit():
            raise GeneralException("EXCEPTION: NOT A DIGIT")
    except GeneralException as error:
        print(error)
        sys.exit(1)

    try:
        operator = input("Enter the operator (+, -, /, *, sqrt, ^, %): ")
        if operator not in ("+", "-", "/", "*", "sqrt", "^", "%"):
            raise GeneralException("EXCEPTION: OPERATOR CAN ONLY BE +, -, /, *, sqrt, ^, or %")
        elif operator == "sqrt":
            num2 = None
            return
    except GeneralException as error:
        print(error)
        sys.exit(1)

    try:
        num2 = input("Enter the second digit (ex. 1 or 1.5): ")
        if not num2.replace(".", "", 1).isdigit():
            raise GeneralException("EXCEPTION: NOT A DIGIT")
    except GeneralException as error:
        print(error)
        sys.exit(1)


def calculate(num1, operator, num2=None):
    num1 = float(num1)
    if num2 is not None:
        num2 = float(num2)
    if operator == "+":
        return num1 + num2
    elif operator == "-":
        return num1 - num2
    elif operator == "/":
        try:
            if num2 == 0:
                raise GeneralException("EXCEPTION: DIVISION BY ZERO")
            else:
                return num1 / num2
        except GeneralException as error:
            print(error)
            sys.exit(1)
    elif operator == "*":
        return num1 * num2
    elif operator == "sqrt":
        return math.sqrt(num1)
    elif operator == "^":
        return num1**num2
    else:
        return num1 % num2


inputData()
print(calculate(num1, operator, num2))