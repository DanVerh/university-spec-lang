import requests
from prettytable import PrettyTable


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
                print("firstname : {}".format(user.get('firstname', 'NULL')))
                print("lastname  : {}".format(user.get('lastname', 'NULL')))
                print("email     : {}".format(user.get('email', 'NULL')))
                print()

    def printUsersTable(self):
        if self.getUsers() == 0:
            print("Error getting the result")
        else:
            users = self.getUsers()
            table = PrettyTable(['Firstname', 'Lastname', 'Email'])
            for user in users:
                table.add_row([user.get('firstname', 'N/A'),
                               user.get('lastname', 'N/A'),
                               user.get('email', 'N/A')])
        print(table)


request = Request()
request.printUsersTable()