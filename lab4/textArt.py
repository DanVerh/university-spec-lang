import sys
import shutil
from termcolor import colored

from .generateArt import generateArt
from lab3.input import *


class TextArt:
    def __init__(self):
        self.text = inputText()
        self.color = inputColor()
        while True:
            self.size = input("Enter the size (big/small): ")
            if self.size == "big" or self.size == "small":
                break

    def __str__(self):
        text = generateArt(self.text, self.size).lower()
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
                with open("./lab4/outputs/output.txt", "w") as file:
                    file.write(text)
        else:
            sys.exit(0)