from .calculator import *


class Lab1:
    pass

    @staticmethod
    def run():
        while True:
            num1, operator, num2 = inputProblem()
            getResult(num1, operator, num2)
            addToHistory(num1, operator, num2)
            close = nextOption()
            if close == "n":
                break
