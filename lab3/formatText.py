import sys
import shutil

import pyfiglet
from termcolor import colored

from fonts import fonts


class TextFormatter:
    def __init__(self):
        self.text = ""
        while not self.text.isalpha():
            self.text = input("Enter the text that you want to format (only English letters): ")
        font = input("Enter the desired font: ")
        if font not in fonts:
            sys.exit(1)
        self.size = input("Enter the text size: ")
        self.color = input("Enter the text color: ")
        self.font = pyfiglet.Figlet(font=font.lower(), width=int(self.size))


    def __str__(self):
        text = self.font.renderText(self.text)
        terminal_width = shutil.get_terminal_size().columns
        padding = " " * ((terminal_width - len(text.strip().split('\n')[0])) // 2)
        self.text = "\n".join(padding + line for line in text.split('\n'))
        return colored(self.text, self.color)
    
    def fileOutput(self):
        text = str(self.text)
        with open("./output.txt", "w") as file:
            file.write(text)