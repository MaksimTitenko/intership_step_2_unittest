import unittest

from calculator import calculator


class CalculatorTest(unittest.TestCase):
    def test_add_0(self):
        result = calculator(1, 2, '+')
        self.assertEqual(result, 3)

    def test_add_2(self):
        result = calculator(3, 1, '-')
        self.assertEqual(result, 2)

    def test_add_3(self):
        result = calculator(10, 2, '/')
        self.assertEqual(result, 5)

    def test_add_4(self):
        result = calculator(8, 4, '*')
        self.assertEqual(result, 32)

    def test_add_5(self):
        result = calculator(5, 2, '**')
        self.assertEqual(result, 25)


if __name__ == '__main__':
    unittest.main()