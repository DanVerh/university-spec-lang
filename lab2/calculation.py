import math


class CalculateException(Exception):
    pass


def add(num1, num2):
    return num1 + num2


def subtract(num1, num2):
    return num1 - num2


def multiply(num1, num2):
    return num1 * num2


def divide(num1, num2):
    try:
        if num2 == 0:
            raise CalculateException("EXCEPTION: DIVISION BY ZERO")
        else:
            return num1 / num2
    except CalculateException as error:
        return error


def sqrt(num1, num2):
    return math.sqrt(num1)


def power(num1, num2):
    return num1 ** num2


def remDiv(num1, num2):
    return num1 % num2


operators = {
    '+': add,
    '-': subtract,
    '*': multiply,
    '/': divide,
    'sqrt': sqrt,
    '^': power,
    '%': remDiv
}


