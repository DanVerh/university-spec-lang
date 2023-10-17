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
    print(historyDict)