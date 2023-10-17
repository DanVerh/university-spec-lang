from calculation import *
from input import *


class CalculateException(Exception):
    pass

num1 = inputNumber()
operator = inputOperator()
num2 = inputNumber()

print(calculate(num1, operator, num2))