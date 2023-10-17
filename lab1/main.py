from calculation import *
from input import *

close = ""

while close != "n":
    num1 = inputNumber()
    operator = inputOperator()
    num2 = inputNumber()

    print(calculate(num1, operator, num2))
    close = input("Do you want to continue? (y/n): ")
    while close not in ("y", "n"):
        if close == "n":
            print("Exiting the program")
            break
        elif close not in ("y", "n"):
            close = input("Please provide the correct input (y/n): ")