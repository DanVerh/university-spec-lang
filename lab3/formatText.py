import sys
import shutil

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
        text = self.font.renderText(self.text)
        terminal_width = shutil.get_terminal_size().columns
        padding = " " * ((terminal_width - len(text.strip().split('\n')[0])) // 2)
        text = "\n".join(padding + line for line in text.split('\n'))
        return colored(text, self.color)