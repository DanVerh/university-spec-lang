import os
import sys

from lab3.input import inputColor
from .drawFigure import *

class Art3D:
    def __init__(self):
        while True:
            self.figure = input("Select the figure (pyramid/cube): ")
            if self.figure == "pyramid" or self.figure == "cube":
                break
        while True:
            self.size = input("Select the figure size (5-50): ")
            if self.size.isdigit():
                self.size = int(self.size)
                if 5 <= self.size <= 50:
                    break

    def printFigure(self):
        if self.figure == "pyramid":
            print("3D Pyramid:")
            draw3dPyramid(self.size)
            print("2D Perspective:")
            draw2dPyramid(self.size)
        else:
            print("3D Cube:")
            draw3dCube(self.size)
            print("2D Perspective:")
            draw2dCube(self.size)

    def saveOutput(self):
        save = ""
        while save not in ("y", "n"):
            save = input("Do you want to save the output to the file (y/n)? ")
            if save == "y":
                os.system('cls' if os.name == 'nt' else 'clear')
                with open("./lab5/outputs/output.txt", "w") as file:
                    sys.stdout = file
                    if self.figure == "pyramid":
                        draw3dPyramid(self.size)
                    else:
                        draw3dCube(self.size)
                    sys.stdout = sys.__stdout__
            else:
                sys.exit(0)