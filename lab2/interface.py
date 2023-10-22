from history import *
from calculator import *

history = History()


class Interface:
    def __init__(self):
        self.option = 0
        while int(self.option) < 1 or int(self.option) > 3:
            self.option = input("Please select the option (1 - Calculator, 2 - See history, 3 - Exit): ")

    def start(self):
        if self.option == "1":
            calculator = Calculator()
            print(calculator)
            history.addResult(calculator)
            del calculator
        elif self.option == "2":
            history.printHistory()
        else:
            print("Exiting")
            sys.exit(0)
