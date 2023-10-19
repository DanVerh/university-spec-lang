from calculator import *

close = ""

while close != "n":
    num1, operator, num2 = inputProblem()
    getResult(num1, operator, num2)
    addToHistory(num1, operator, num2)
    close = nextOption()
