from .unitTests import *
from .apiRequests import *
import sys


class Interface:
    def __init__(self):
        self.request = Request()



    def start(self):
        while True:
            option = input("Please select the option (1 - Get user table, 2 - Get user list, 3 - Get user by name, 4 - Run unit test, 5 - Print request history, 6 - Exit): ")
            if not option.isdigit():
                print("Enter number 1-6")
            elif not 1 <= int(option) <= 6:
                print("Enter number 1-6")
            else:
                break

        if option == "1":
            self.request.printUsersTable()
        elif option == "2":
            self.request.printUsersList()
        elif option == "3":
            self.request.printOneUser()
        elif option == "4":
            runTest()
        elif option == "5":
            self.request.history.printHistory()
        elif option == "6":
            print("Exiting")
            sys.exit(0)
