import csv
import json

import requests
from prettytable import PrettyTable
from datetime import datetime
from termcolor import colored
from lab3 import inputColor

class InputException(Exception):
    pass

class Request:
    def __init__(self):
        self.url = "https://jsonplaceholder.org/users"
        self.color = inputColor()

    def getUsers(self):
        response = requests.get(self.url)
        if response.status_code == 200:
            users = response.json()
            return users
        else:
            print("Error:", response.status_code)
            print("Response content:", response.text)
            return 0

    def getUserByUsername(self):
        users = self.getUsers()
        username = input("Enter the username to search: ")
        if users:
            filteredUsers = [user for user in users if user.get('login', {}).get('username') == username]
            if filteredUsers:
                return filteredUsers[0]
            else:
                print(f"No user found with username '{username}'")
                return None
        else:
            print("No users retrieved.")
            return None

    def printUsersJSON(self):
        if self.getUsers() == 0:
            print("Error getting the result")
        else:
            print(self.getUsers())

    def printUsersList(self):
        if self.getUsers() == 0:
            print("Error getting the result")
        else:
            users = self.getUsers()
            for user in users:
                try:
                    if user.get('birthDate', 'NULL') != "NULL":
                        bithdate = datetime.strptime(user.get('birthDate', 'NULL'), "%Y-%m-%d")
                    else:
                        raise InputException("EXCEPTION: DATE FORMAT IS INVALID")
                except InputException as error:
                    print(error)
                    break
                formattedBirthdate = bithdate.strftime("%d %B %Y")
                print(colored("firstname :", self.color), user.get('firstname', 'NULL'))
                print(colored("lastname  :", self.color), user.get('lastname', 'NULL'))
                print(colored("email     :", self.color), user.get('email', 'NULL'))
                print(colored("username  :", self.color), user.get('login', {}).get('username', 'NULL'))
                print(colored("birthdate :", self.color), formattedBirthdate)
                print()

    def printUsersTable(self):
        if self.getUsers() == 0:
            print("Error getting the result")
        else:
            users = self.getUsers()
            table = PrettyTable(['Firstname', 'Lastname', 'Email', 'Username', 'Birthdate'])
            colored_headers = [colored(header, self.color) for header in table.field_names]
            table.field_names = colored_headers
            for user in users:
                try:
                    if user.get('birthDate', 'NULL') != "NULL":
                        bithdate = datetime.strptime(user.get('birthDate', 'NULL'), "%Y-%m-%d")
                    else:
                        raise InputException("EXCEPTION: DATE FORMAT IS INVALID")
                except InputException as error:
                    print(error)
                    break
                formattedBirthdate = bithdate.strftime("%d %B %Y")
                table.add_row([user.get('firstname', 'N/A'),
                               user.get('lastname', 'N/A'),
                               user.get('email', 'N/A'),
                               user.get('login', {}).get('username', 'N/A'),
                               formattedBirthdate])
            print(table)
            self.saveOutput(users)

    def printOneUser(self):
        user = self.getUserByUsername()
        if user is not None:
            try:
                if user.get('birthDate', 'NULL') != "NULL":
                    bithdate = datetime.strptime(user.get('birthDate', 'NULL'), "%Y-%m-%d")
                else:
                    raise InputException("EXCEPTION: DATE FORMAT IS INVALID")
            except InputException as error:
                print(error)
            formattedBirthdate = bithdate.strftime("%d %B %Y")
            print(colored("firstname :", self.color), user.get('firstname', 'NULL'))
            print(colored("lastname  :", self.color), user.get('lastname', 'NULL'))
            print(colored("email     :", self.color), user.get('email', 'NULL'))
            print(colored("username  :", self.color), user.get('login', {}).get('username', 'NULL'))
            print(colored("birthdate :", self.color), formattedBirthdate)
            print()
            self.saveOutput(user)

    def saveOutput(self, output):
        while True:
            format = input("Save the file as 1 - JSON, 2 - CSV, 3 - TXT, 4 - Exit: ")
            if format == "1":
                if output:
                    with open('./lab7/outputs/output.json', 'w') as json_file:
                        json.dump(output, json_file, indent=2)
                    print(f"Users data saved to ./lab7/outputs/output.json")
                else:
                    print("No users to save")
            elif format == "2":
                if output:
                    with open('./lab7/outputs/output.csv', 'w', newline='') as csv_file:
                        writer = csv.writer(csv_file)
                        writer.writerows([user.values() for user in output])
                    print(f"Users data saved to ./lab7/outputs/output.csv")
                else:
                    print("No users to save.")
            elif format == "3":
                if output:
                    with open('./lab7/outputs/output.txt', 'w') as txt_file:
                        txt_file.write(str(output))
                    print(f"Users data saved to ./lab7/outputs/output.txt")
                else:
                    print("No users to save.")
            elif format == "4":
                break
            else:
                print("Enter number 1 - 4")



request = Request()
request.printUsersTable()