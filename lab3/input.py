from .allowedInput import *


class InputException(Exception):
    pass


def inputText():
    text = ""
    while not text.isalpha():
        try:
            text = input("Enter the text that you want to format (only English letters): ")
            if not text.isalpha():
                raise InputException("EXCEPTION: PROVIDE ONLY ENGLISH LETTERS")
        except InputException as error:
            print(error)
    return text


def inputSize(text):
    size = ""
    while not size.isdigit() or int(size) < len(text):
        try:
            size = input("Enter the desired size: ")
            if not size.isdigit() or int(size) < len(text):
                raise InputException("EXCEPTION: PROVIDE ONLY POSITIVE INTEGER > TEXT LENGTH")
        except InputException as error:
            print(error)
    return size


def inputColor():
    color = ""
    while color not in colors:
        try:
            color = input("Enter the desired color: ")
            if color not in colors:
                raise InputException("EXCEPTION: PROVIDE ONLY ALLOWED COLOR")
        except InputException as error:
            print(error)
    return color


def inputFont():
    font = ""
    while font not in fonts:
        try:
            font = input("Enter the desired font: ")
            if font not in fonts:
                raise InputException("EXCEPTION: PROVIDE ONLY ALLOWED FONT")
        except InputException as error:
            print(error)
    return font
