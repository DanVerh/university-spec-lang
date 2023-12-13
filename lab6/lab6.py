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
        self.assertEqual(operators['/'](6, 3), 2)
        self.assertEqual(operators['/'](0, 5), 0)

    def test_sqrt(self):
        self.assertEqual(operators['sqrt'](9, None), 3)
        self.assertEqual(operators['sqrt'](16, None), 4)
        self.assertEqual(operators['sqrt'](0, None), 0)

    def test_power(self):
        self.assertEqual(operators['^'](2, 3), 8)
        self.assertEqual(operators['^'](5, 0), 1)
        self.assertEqual(operators['^'](0, 2), 0)

    def test_remDiv(self):
        self.assertEqual(operators['%'](10, 3), 1)
        self.assertEqual(operators['%'](15, 7), 1)
        self.assertEqual(operators['%'](8, 2), 0)


def lab6():
    test_suite = unittest.TestLoader().loadTestsFromTestCase(TestCalculatorFunctions)
    unittest.TextTestRunner().run(test_suite)