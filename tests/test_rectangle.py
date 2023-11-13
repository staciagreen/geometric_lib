import rectangle
import unittest

DELTA = 1e-15


# class with test for funcs from file "rectangle.py"
class RectangleTestCase(unittest.TestCase):

    # test with zero result
    def test_area_zero_1(self):
        with self.assertRaises(ArithmeticError):
            rectangle.area(2, 0)

    # test with float result
    def test_area_float_1(self):
        res = rectangle.area(1.10101, 9.333333)
        self.assertEqual(res, 10.27609296633, DELTA)

    # test with negative parameter
    def test_area_negative_1(self):
        with self.assertRaises(ArithmeticError):
            rectangle.area(2, -2)

    # test with regular numbers

    def test_area_regular_1(self):
        res = rectangle.area(23, 2)
        self.assertEqual(res, 46)

    # test with long numbers

    def test_area_long_1(self):
        res = rectangle.area(123456789, 88888888)
        self.assertEqual(res, 10973936690260632)

    # test with zero result

    def test_perimeter_zero_1(self):
        with self.assertRaises(ArithmeticError):
            rectangle.perimeter(0, 0)

    # test with float result

    def test_perimeter_float_1(self):
        res = rectangle.perimeter(1.1, 9.333333)
        self.assertEqual(res, 20.866666)

    # test with one zero parameter

    def test_perimeter_zero_1(self):
        with self.assertRaises(ArithmeticError):
            rectangle.perimeter(5, 0)

    # test with negative parameter
    def test_area_negative_1(self):
        with self.assertRaises(ArithmeticError):
            rectangle.perimeter(-12, 6)

    # test with regular numbers

    def test_perimeter_regular_1(self):
        res = rectangle.perimeter(70, 2)
        self.assertEqual(res, 144)

    # test with long numbers

    def test_perimeter_long_1(self):
        res = rectangle.perimeter(123456789000, 88888888000)
        self.assertEqual(res, 424691354000)
