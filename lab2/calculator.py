import sys

from input import *
from calculation import *


class Calculator:
    def __init__(self):
        self.num1 = inputNumber()
        self.operator = inputOperator()
        if self.operator != "sqrt":
            self.num2 = inputNumber()
        else:
            self.num2 = None

    def __str__(self):
        if self.num2 is not None:
            return f"{self.num1} {self.operator} {self.num2} = {self.calculate()}"
        else:
            return f"{self.num1} {self.operator} = {self.calculate()}"

    def calculate(self, num2=None):
        num1 = float(self.num1)
        if self.num2 is not None:
            num2 = float(self.num2)
        return operators.get(self.operator)(num1, num2)

    #def nextOption(self, history):
    #    close = input("Do you want to continue or see history? (y/n/h): ")
    #    while close not in ("y", "n"):
    #        if close == "n":
    #            print("Exiting the program")
    #            sys.exit(0)
    #        elif close == "y":
    #            break
    #        elif close == "h":
    #
    #            close = input("Do you want to continue? (y/n): ")
    #        else:
    #            close = input("Please provide the correct input (y/n/h): ")
    #    return close