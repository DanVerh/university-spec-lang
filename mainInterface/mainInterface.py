class MainInterface:
    def __init__(self):
        while True:
            self.option = input("Enter lab 1-8, 9 - exit: ")
            if self.option.isdigit() and 1 <= int(self.option) <= 9:
                break
            else:
                print("Enter 1-9")


def selectLab():
    interface = MainInterface()
    return interface.option

