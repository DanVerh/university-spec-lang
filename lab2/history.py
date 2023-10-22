from calculator import *

from collections import OrderedDict


class History:
    def __init__(self):
        self.historyDict = OrderedDict()
        self.historyMax = ""
        while not self.historyMax.isdigit():
            try:
                self.historyMax = input("Enter the maximum amount of calculate records that you want to save: ")
                if not self.historyMax.isdigit():
                    raise InputException("EXCEPTION: NOT A DIGIT")
            except InputException as error:
                print(error)

    def addResult(self, calculator):
        if calculator.operator != "sqrt":
            problem = calculator.num1 + calculator.operator + calculator.num2
        else:
            problem = calculator.num1 + calculator.operator
        result = calculator.calculate()
        self.historyDict[problem] = result
        if len(self.historyDict) > int(self.historyMax):
            self.historyDict.popitem(last=False)

    def printHistory(self):
        for index, problem in enumerate(self.historyDict):
            index += 1
            print(f"{index}. {problem} = {self.historyDict[problem]}")

#def getResultByIndex(historyIndex):
#    for index, problem in enumerate(historyDict):
#        if index == historyIndex:
#            print("num1 =", historyDict[problem])
#            return historyDict[problem]
#