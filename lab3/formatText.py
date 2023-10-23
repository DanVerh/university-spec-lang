import sys
import pyfiglet
from termcolor import colored

from fonts import fonts


class TextFormatter:
    def __init__(self):
        self.text = input("Enter the text that you want to format: ")
        font = input("Enter the desired font: ")
        if font not in fonts:
            sys.exit(1)
        self.font = pyfiglet.Figlet(font=font.lower())
        self.color = input("Enter the text color: ")

    def __str__(self):
        return colored(self.font.renderText(self.text), self.color)
