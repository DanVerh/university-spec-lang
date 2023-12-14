import sys

from lab1 import Lab1
from lab2 import Lab2
from lab3 import Lab3
from lab4 import Lab4
from lab5 import Lab5
from lab6 import Lab6
from lab7 import Lab7
from lab8 import Lab8


class MainInterface:
    def __init__(self):
        while True:
            self.option = input("Enter lab 1-8, 9 - exit: ")
            if self.option.isdigit() and 1 <= int(self.option) <= 9:
                break
            else:
                print("Enter 1-9")

    def runInterface(self):
        if self.option == "1":
            lab1 = Lab1()
            lab1.run()
        elif self.option == "2":
            lab2 = Lab2()
            lab2.run()
        elif self.option == "3":
            lab3 = Lab3()
            lab3.run()
        elif self.option == "4":
            lab4 = Lab4()
            lab4.run()
        elif self.option == "5":
            lab5 = Lab5()
            lab5.run()
        elif self.option == "6":
            lab6 = Lab6()
            lab6.run()
        elif self.option == "7":
            lab7 = Lab7()
            lab7.run()
        elif self.option == "8":
            lab8 = Lab8()
            lab8.run()
        else:
            print("Exiting")
            sys.exit(0)


