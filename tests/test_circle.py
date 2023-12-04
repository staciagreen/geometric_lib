import circle
import unittest

DELTA = 1e-15


# class with test for funcs from file "circle.py"
class CircleTestCase(unittest.TestCase):
    # test with zero result

    def test_area_zero_1(self):
        with self.assertRaises(ArithmeticError):
            circle.area(0)

    # test with float result

    def test_area_float_1(self):
        res = circle.area(1.10101)
        self.assertEqual(res, 3.8083109344585924, DELTA)

    # test with negative parameter
    def test_area_negative_1(self):
        with self.assertRaises(ArithmeticError):
            circle.area(-100000)

    # test with regular numbers

    def test_area_regular_1(self):
        res = circle.area(23)
        self.assertAlmostEqual(res, 1661.9025137490005)

    # test with long numbers

    def test_area_long_1(self):
        res = circle.area(123456789000)
        self.assertAlmostEqual(res, 4.788283183070884e+22)

    # test with zero result

    def test_perimeter_zero_1(self):
        with self.assertRaises(ArithmeticError):
            circle.perimeter(0)

    # test with float parameter
    def test_perimeter_float_1(self):
        res = circle.perimeter(1.10101)
        self.assertEqual(res, 6.9178498550577965, DELTA)

    # test with negative parameter
    def test_perimeter_negative_1(self):
        with self.assertRaises(ArithmeticError):
            circle.perimeter(-100000)

    # test with regular numbers

    def test_perimeter_regular_1(self):
        res = circle.perimeter(70)
        self.assertAlmostEqual(res, 439.822971502571)

    # test with long numbers

    def test_perimeter_long_1(self):
        res = circle.perimeter(123456789000)
        self.assertAlmostEqual(res, 775701882716.3704)
