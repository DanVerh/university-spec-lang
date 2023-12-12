from .calculator import *


def lab1():
    while True:
        num1, operator, num2 = inputProblem()
        getResult(num1, operator, num2)
        addToHistory(num1, operator, num2)
        close = nextOption()
        if close == "n":
            break
