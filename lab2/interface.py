from history import *
from calculator import *

history = History()


class Interface:
    def __init__(self):
        self.option = 0
        while int(self.option) < 1 or int(self.option) > 3:
            try:
                self.option = input("Please select the option (1 - Calculator, 2 - See history, 3 - Exit): ")
                if not str(self.option).isdigit():
                    self.option = 0
                    raise InputException("EXCEPTION: INPUT CAN ONLY BE 1, 2 or 3")
                elif int(self.option) < 1 or int(self.option) > 3:
                    raise InputException("EXCEPTION: INPUT CAN ONLY BE 1, 2 or 3")
            except InputException as error:
                print(error)

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
