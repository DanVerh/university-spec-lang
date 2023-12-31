import sys
import shutil

import pyfiglet
from termcolor import colored

from .input import *


class TextFormatter:
    def __init__(self):
        self.text = inputText()
        self.color = inputColor()
        self.font = pyfiglet.Figlet(font=inputFont().lower(), width=int(inputSize(self.text)))

    def __str__(self):
        text = self.font.renderText(self.text)
        terminal_width = shutil.get_terminal_size().columns
        padding = " " * ((terminal_width - len(text.strip().split('\n')[0])) // 2)
        self.text = "\n".join(padding + line for line in text.split('\n'))
        return colored(self.text, self.color)
    
    def saveOutput(self):
        save = ""
        while save not in ("y", "n"):
            save = input("Do you want to save the output to the file (y/n)? ")
            if save == "y":
                text = str(self.text)
                with open("./lab3/outputs/output.txt", "w") as file:
                    file.write(text)
        else:
            sys.exit(0)