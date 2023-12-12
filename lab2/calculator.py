from .input import *
from .calculation import *


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
