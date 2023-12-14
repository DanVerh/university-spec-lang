import sys

from lab1 import lab1
from lab2 import lab2
from lab3 import lab3
from lab4 import lab4
from lab5 import lab5
from lab6 import *
from lab7 import *
from lab8 import *
from mainInterface import *


def main():
    option = selectLab()
    if option == "1":
        lab1()
    elif option == "2":
        lab2()
    elif option == "3":
        lab3()
    elif option == "4":
        lab4()
    elif option == "5":
        lab5()
    elif option == "6":
        lab6()
    elif option == "7":
        lab7()
    elif option == "8":
        lab8()
    else:
        print("Exiting")
        sys.exit(0)

if __name__ == "__main__":
    main()
