from .history import *
from .input import *
from .calculation import *

count = 0


def inputProblem():
    historyLen = len(historyDict)
    if count == 0:
        num1 = inputNumber()
    else:
        option = "-1"
        while not 0 <= int(option) <= len(historyDict) + 1:
            option = input(f"Input manually num1 - 0 or choose index from history up to {historyLen}: ")
        if option == "0":
            num1 = inputNumber()
        else:
            num1 = str(getResultByIndex(int(option)-1))
    operator = inputOperator()
    if operator != "sqrt":
        num2 = inputNumber()
    else:
        num2 = None
    return num1, operator, num2


def getResult(num1, operator, num2=None):
    result = calculate(num1, operator, num2)
    print(result)
    return result


def addToHistory(num1, operator, num2):
    global count
    addResult(num1, operator, num2)
    count += 1


def nextOption():
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
    return close
