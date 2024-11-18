import unittest
from calculator import Calculator

class TestCalculator(unittest.TestCase):

    def setUp(self):
        self.calc = Calculator()

    # test add()
    def test_add_positive_numbers(self):
        self.assertEqual(self.calc.add(1, 2), 3)  # 1 + 2 = 3

    def test_add_negative_numbers(self):
        self.assertEqual(self.calc.add(-1, -2), -3)  # -1 + (-2) = -3

    # test subtract()
    def test_subtract_positive_result(self):
        self.assertEqual(self.calc.subtract(5, 3), 2)  # 5 - 3 = 2

    def test_subtract_negative_result(self):
        self.assertEqual(self.calc.subtract(3, 5), -2)  # 3 - 5 = -2

    # test multiply()
    def test_multiply_positive_numbers(self):
        self.assertEqual(self.calc.multiply(3, 4), 12)  # 3 * 4 = 12

    def test_multiply_with_zero(self):
        self.assertEqual(self.calc.multiply(5, 0), 0)  # 5 * 0 = 0

    # test divide()
    def test_divide_exact_result(self):
        self.assertEqual(self.calc.divide(10, 2), 5)  # 10 / 2 = 5

    def test_divide_floor_result(self):
        self.assertEqual(self.calc.divide(7, 2), 3)  # 7 / 2 = 3 (round down)

    # test modulo()
    def test_modulo_zero_remainder(self):
        self.assertEqual(self.calc.modulo(10, 2), 0)  # 10 % 2 = 0

    def test_modulo_nonzero_remainder(self):
        self.assertEqual(self.calc.modulo(10, 3), 1)  # 10 % 3 = 1

if __name__ == '__main__':
    unittest.main()