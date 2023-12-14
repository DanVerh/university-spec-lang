from .interface import *
from .history import History


class Lab2:
    pass

    @staticmethod
    def run():
        history = History()
        while True:
            interface = Interface()
            interface.start(history)
