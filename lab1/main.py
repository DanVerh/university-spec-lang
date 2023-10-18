from calculation import *
from input import *
from history import *

close = ""
count = 0

while close != "n":
    if count == 0:
        num1 = inputNumber()
    else:
        option = "-1"
        while not 0 <= int(option) <= 10:
            option = input("Input manually num1 - 0, take from history - 1-10: ")
        if option == "0":
            num1 = inputNumber()
        else:
            num1 = str(getResultByIndex(int(option)-1))
    operator = inputOperator()
    if operator != "sqrt":
        num2 = inputNumber()
    else:
        num2 = None

    print(calculate(num1, operator, num2))
    addResult(num1, operator, num2)
    count += 1
    close = input("Do you want to continue or see history? (y/n/h): ")
    while close not in ("y", "n"):
        if close == "n":
            print("Exiting the program")
            break
        elif close == "y":
            break
        elif close == "h":
            printHistory()
            close = input("Do you want to continue? (y/n): ")
        else:
            close = input("Please provide the correct input (y/n/h): ")