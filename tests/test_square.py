import square
import unittest

DELTA = 1e-15


# class with test for funcs from file "square.py"
class SquareTestCase(unittest.TestCase):
    # test with zero result

    def test_area_zero_1(self):
        with self.assertRaises(ArithmeticError):
            square.area(0)

    # test with float result

    def test_area_float_1(self):
        res = square.area(1.10101)
        self.assertEqual(res, 1.2122230201000002, DELTA)

    # test with negative parameter

    def test_area_negative_1(self):
        with self.assertRaises(ArithmeticError):
            square.area(-100000)

    # test with regular numbers

    def test_area_regular_1(self):
        res = square.area(23)
        self.assertEqual(res, 529)

    def test_small_numbers_area_regular_2(self):
        res = square.area(100)
        self.assertEqual(res, 10000)

    def test_area_3(self):
        res = square.area(3)
        self.assertEqual(res, 9)

    # test with long numbers

    def test_area_long_1(self):
        res = square.area(123456789000)
        self.assertEqual(res, 15241578750190521000000)

    # test with zero result

    def test_perimeter_zero_1(self):
        with self.assertRaises(ArithmeticError):
            square.perimeter(0)

    # test with float result

    def test_perimeter_float_1(self):
        res = square.perimeter(1.101067678981)
        self.assertEqual(res, 4.404270715924, DELTA)

    # test with negative parameter

    def test_perimeter_negative_1(self):
        with self.assertRaises(ArithmeticError):
            square.perimeter(-100000)

    def test_perimeter_negative_2(self):
        with self.assertRaises(ArithmeticError):
            square.perimeter(-1)

    # test with regular numbers

    def test_perimeter_regular_1(self):
        res = square.perimeter(70)
        self.assertEqual(res, 280)

    # test with long numbers

    def test_perimeter_long_1(self):
        res = square.perimeter(123456789000)
        self.assertEqual(res, 493827156000)
