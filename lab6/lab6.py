import unittest
from lab2.calculation import operators

class TestCalculatorFunctions(unittest.TestCase):

    def test_add(self):
        self.assertEqual(operators['+'](3, 5), 8)
        self.assertEqual(operators['+'](0, 0), 0)
        self.assertEqual(operators['+'](-3, 5), 2)

    def test_subtract(self):
        self.assertEqual(operators['-'](3, 5), -2)
        self.assertEqual(operators['-'](0, 0), 0)
        self.assertEqual(operators['-'](-3, 5), -8)

    def test_multiply(self):
        self.assertEqual(operators['*'](3, 5), 15)
        self.assertEqual(operators['*'](0, 0), 0)
        self.assertEqual(operators['*'](-3, 5), -15)

    def test_divide(self):
        self.assertEqual(operators['/'](6, 0), 2)
        self.assertEqual(operators['/'](0, 5), 0)


def lab6():
    test_suite = unittest.TestLoader().loadTestsFromTestCase(TestCalculatorFunctions)
    unittest.TextTestRunner().run(test_suite)