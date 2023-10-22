from calculator import *
from history import *

history = History()
calculator = Calculator()
history.addResult(calculator)
history.printHistory()