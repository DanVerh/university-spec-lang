from collections import OrderedDict


class History:
    def __init__(self):
        self.historyDict = OrderedDict()

    def addResult(self, call, save):
        if save == "1":
            self.historyDict[call] = "Saved to JSON"
        elif save == "2":
            self.historyDict[call] = "Saved to CSV"
        elif save == "3":
            self.historyDict[call] = "Saved to TXT"
        else:
            self.historyDict[call] = "Not saved"

    def printHistory(self):
        for index, call in enumerate(self.historyDict):
            index += 1
            print(f"{index}. {call}(): {self.historyDict[call]}")