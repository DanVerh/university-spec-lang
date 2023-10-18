from calculation import *
from input import *
from history import *

close = ""

while close != "n":
    num1 = inputNumber()
    operator = inputOperator()
    if operator != "sqrt":
        num2 = inputNumber()
    else:
        num2 = None

    print(calculate(num1, operator, num2))
    addResult(num1, operator, num2)
    close = input("Do you want to continue? (y/n): ")
    while close not in ("y", "n"):
        if close == "n":
            print("Exiting the program")
            break
        elif close not in ("y", "n"):
            close = input("Please provide the correct input (y/n): ")

printHistory()