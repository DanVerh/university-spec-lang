from .tests import *


class Lab6:
    pass

    @staticmethod
    def run():
        test_suite = unittest.TestLoader().loadTestsFromTestCase(TestCalculatorFunctions)
        unittest.TextTestRunner().run(test_suite)