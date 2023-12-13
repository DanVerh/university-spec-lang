import unittest
from .apiRequests import *


class TestCalculatorFunctions(unittest.TestCase):

    def test_getCallingFunction(self):
        test_request = Request()
        self.assertEqual(test_request.getCallingFunction(), "_callTestMethod")

    def test_getUserByUsername(self):
        test_request = Request()
        self.assertEqual(test_request.getUserByUsername(), "johndoe")


def runTest():
    test_suite = unittest.TestLoader().loadTestsFromTestCase(TestCalculatorFunctions)
    unittest.TextTestRunner().run(test_suite)