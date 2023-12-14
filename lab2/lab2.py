from .interface import *
from .history import History


def lab2():
    history = History()
    while True:
        interface = Interface()
        interface.start(history)
