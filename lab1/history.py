from calculation import *
from input import InputException

from collections import OrderedDict

historyDict = OrderedDict()

def inputMaxHistory():
    historyMax = ""
    while not historyMax.isdigit():
        try:
            historyMax = input("Enter the maximum amount of calculate records that you want to save: ")
            if not historyMax.isdigit():
                raise InputException("EXCEPTION: NOT A DIGIT")
        except InputException as error:
            print(error)
    return historyMax


def addResult(num1, operator, num2):
    global historyMax
    if len(historyDict) == 0:
        historyMax = inputMaxHistory()
    if operator != "sqrt":
        problem = num1 + operator + num2
        result = calculate(num1, operator, num2)
    else:
        problem = num1 + operator
        result = calculate(num1, operator)
    historyDict[problem] = result
    if len(historyDict) > int(historyMax):
        historyDict.popitem(last=False)


def printHistory():
    for index, problem in enumerate(historyDict):
        index += 1
        print(f"{index}. {problem} = {historyDict[problem]}")


def getResultByIndex(historyIndex):
    for index, problem in enumerate(historyDict):
        if index == historyIndex:
            print("num1 =", historyDict[problem])
            return historyDict[problem]
