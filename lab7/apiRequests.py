import requests
from prettytable import PrettyTable
from datetime import datetime

class InputException(Exception):
    pass

class Request:
    def __init__(self):
        self.url = "https://jsonplaceholder.org/users"

    def getUsers(self):
        response = requests.get(self.url)
        if response.status_code == 200:
            users = response.json()
            return users
        else:
            print("Error:", response.status_code)
            print("Response content:", response.text)
            return 0

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
                print("firstname : {}".format(user.get('firstname', 'NULL')))
                print("lastname  : {}".format(user.get('lastname', 'NULL')))
                print("email     : {}".format(user.get('email', 'NULL')))
                print("username  : {}".format(user.get('login', {}).get('username', 'NULL')))
                print("birthdate : {}".format(formattedBirthdate))
                print()

    def printUsersTable(self):
        if self.getUsers() == 0:
            print("Error getting the result")
        else:
            users = self.getUsers()
            table = PrettyTable(['Firstname', 'Lastname', 'Email', 'Username', 'Birthdate'])
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

    #def printOneUser(self):


request = Request()
request.printUsersTable()