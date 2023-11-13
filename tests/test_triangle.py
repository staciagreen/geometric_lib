import triangle
import unittest

DELTA = 1e-15


# class with test for funcs from file "triangle.py"
class TriangleTestCase(unittest.TestCase):
    # test with zero result

    def test_area_zero_1(self):
        with self.assertRaises(ArithmeticError):
            triangle.area(12, 0)

    # test with float result

    def test_area_float_1(self):
        res = triangle.area(1.10101, 1.8)
        self.assertEqual(res, 0.990909, DELTA)

    # test with negative parameter
    def test_area_negative_1(self):
        with self.assertRaises(ArithmeticError):
            triangle.area(-12, 6)

    def test_area_negative_2(self):
        with self.assertRaises(ArithmeticError):
            triangle.area(4, -21)

    # test with regular numbers

    def test_area_regular_1(self):
        res = triangle.area(23, 2)
        self.assertEqual(res, 23)

    # test with long numbers

    def test_area_long_1(self):
        res = triangle.area(123456789, 88888888)
        self.assertEqual(res, 5486968345130316.0)

    # test with zero result

    def test_perimeter_zero_1(self):
        with self.assertRaises(ArithmeticError):
            triangle.perimeter(0, 3, 0)

    # test with float result

    def test_perimeter_float_1(self):
        res = triangle.perimeter(100.10101, 100.8, 45.7890)
        self.assertEqual(res, 246.69000999999997, DELTA)

    # test with negative parameter

    def test_perimeter_negative_1(self):
        with self.assertRaises(ArithmeticError):
            triangle.perimeter(-100000, 1, 4)

    # test with regular numbers

    def test_perimeter_regular_1(self):
        res = triangle.perimeter(39, 2, 40)
        self.assertEqual(res, 81)

    def test_perimeter_regular_2(self):
        with self.assertRaises(ArithmeticError):
            triangle.perimeter(1, 10, 1)

    # test with long numbers

    def test_perimeter_long_1(self):
        res = triangle.perimeter(123456789000, 88888888000, 34567901019)
        self.assertEqual(res, 246913578019)
