from calculation import *

from collections import OrderedDict

historyDict = OrderedDict()


def addResult(num1, operator, num2):
    if operator != "sqrt":
        problem = num1 + operator + num2
        result = calculate(num1, operator, num2)
    else:
        problem = num1 + operator
        result = calculate(num1, operator)
    historyDict[problem] = result


def printHistory():
    for index, problem in enumerate(historyDict):
        index += 1
        print(f"{index}. {problem} = {historyDict[problem]}")


def getResultByIndex(historyIndex):
    for index, problem in enumerate(historyDict):
        if index == historyIndex:
            print("num1 =", historyDict[problem])
            return historyDict[problem]
