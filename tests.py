import unittest
import rectangle
import circle
import square
import triangle

DELTA = 1e-15;


# class with test for funcs from file "rectangle.py"
class RectangleTestCase(unittest.TestCase):

    # tests with zero result
    def test_area_zero_1(self):
        res = rectangle.area(2, 0)
        self.assertEqual(res, "inappropriate input parameters")

    def test_area_zero_2(self):
        res = rectangle.area(0, 2)
        self.assertEqual(res, "inappropriate input parameters")

    def test_area_zero_3(self):
        res = rectangle.area(0, 0)
        self.assertEqual(res, "inappropriate input parameters")

    # tests with float result
    def test_area_float_1(self):
        res = rectangle.area(1.10101, 9.333333)
        self.assertEqual(res, 10.27609296633, DELTA)

    # tests with negative parameter
    def test_area_negative_1(self):
        res = rectangle.area(2, -2)
        self.assertEqual(res, "inappropriate input parameters")

    def test_area_negative_2(self):
        res = rectangle.area(-10, 2)
        self.assertEqual(res, "inappropriate input parameters")

    # tests with regular numbers

    def test_area_regular_1(self):
        res = rectangle.area(23, 2)
        self.assertEqual(res, 46)

    def test_area_regular_2(self):
        res = rectangle.area(100, 5)
        self.assertEqual(res, 500)

    def test_area_regular_3(self):
        res = rectangle.area(3, 3)
        self.assertEqual(res, 9)

    # tests with long numbers

    def test_area_long_1(self):
        res = rectangle.area(123456789, 88888888)
        self.assertEqual(res, 10973936690260632)

    def test_area_long_2(self):
        res = rectangle.area(10973936690260632, 2)
        self.assertEqual(res, 21947873380521264)

    def test_area_long_3(self):
        res = rectangle.area(123456789, 21947873380521264)
        self.assertEqual(res, 2709613972937730399661296)

    # tests with zero result

    def test_perimeter_zero_1(self):
        res = rectangle.perimeter(0, 0)
        self.assertEqual(res, "inappropriate input parameters")

    # tests with float result

    def test_perimeter_float_1(self):
        res = rectangle.perimeter(1.1, 9.333333)
        self.assertEqual(res, 20.866666)

    # tests with one zero parameter

    def test_perimeter_zero_2(self):
        res = rectangle.perimeter(5, 0)
        self.assertEqual(res, "inappropriate input parameters")

    def test_perimeter_zero_3(self):
        res = rectangle.perimeter(0, 7345)
        self.assertEqual(res, "inappropriate input parameters")

    # tests with negative parameter
    def test_area_negative_1(self):
        res = rectangle.perimeter(-12, 6)
        self.assertEqual(res, "inappropriate input parameters")

    def test_area_negative_2(self):
        res = rectangle.perimeter(4, -21)
        self.assertEqual(res, "inappropriate input parameters")

    def test_area_negative_3(self):
        res = rectangle.perimeter(-4, -21)
        self.assertEqual(res, "inappropriate input parameters")

    # tests with regular numbers

    def test_perimeter_regular_1(self):
        res = rectangle.perimeter(70, 2)
        self.assertEqual(res, 144)

    def test_perimeter_regular_2(self):
        res = rectangle.perimeter(100, 5)
        self.assertEqual(res, 210)

    def test_perimeter_regular_3(self):
        res = rectangle.perimeter(3, 3)
        self.assertEqual(res, 12)

    # tests with long numbers

    def test_perimeter_long_1(self):
        res = rectangle.perimeter(123456789000, 88888888000)
        self.assertEqual(res, 424691354000)

    def test_perimeter_long_2(self):
        res = rectangle.perimeter(10973936690260632, 2)
        self.assertEqual(res, 21947873380521268)

    def test_perimeter_long_3(self):
        res = rectangle.perimeter(123456789, 21947873380521264)
        self.assertEqual(res, 43895747007956106)

    # class with test for funcs from file "circle.py"


class CircleTestCase(unittest.TestCase):
    # tests with zero result

    def test_area_zero_1(self):
        res = circle.area(0)
        self.assertEqual(res, "inappropriate input parameters")

    # tests with float result

    def test_area_float_1(self):
        res = circle.area(1.10101)
        self.assertEqual(res, 3.8083109344585924, DELTA)

    # tests with negative parameter
    def test_area_negative_1(self):
        res = circle.area(-100000)
        self.assertEqual(res, "inappropriate input parameters")

    def test_area_negative_2(self):
        res = circle.area(-1)
        self.assertEqual(res, "inappropriate input parameters")

    # tests with regular numbers

    def test_area_regular_1(self):
        res = circle.area(23)
        self.assertAlmostEqual(res, 1661.9025137490005)

    def test_area_regular_2(self):
        res = circle.area(100)
        self.assertAlmostEqual(res, 31415.926535897932)

    def test_area_regular_3(self):
        res = circle.area(3)
        self.assertAlmostEqual(res, 28.274333882308138)

    # tests with long numbers

    def test_area_long_1(self):
        res = circle.area(123456789000)
        self.assertAlmostEqual(res, 4.788283183070884e+22)

    def test_area_long_2(self):
        res = circle.area(10973936690260632)
        self.assertAlmostEqual(res, 3.783334785031286e+32)

    def test_area_long_3(self):
        res = circle.area(1000000000)
        self.assertAlmostEqual(res, 3.1415926535897933e+18)

    # tests with zero result

    def test_perimeter_zero_1(self):
        res = circle.perimeter(0)
        self.assertEqual(res, "inappropriate input parameters")

    # tests with float parameter
    def test_perimeter_float_1(self):
        res = circle.perimeter(1.10101)
        self.assertEqual(res, 6.9178498550577965, DELTA)

    # tests with negative parameter
    def test_perimeter_negative_1(self):
        res = circle.perimeter(-100000)
        self.assertEqual(res, "inappropriate input parameters")

    def test_perimeter_negative_2(self):
        res = circle.perimeter(-1)
        self.assertEqual(res, "inappropriate input parameters")

    # tests with regular numbers

    def test_perimeter_regular_1(self):
        res = circle.perimeter(70)
        self.assertAlmostEqual(res, 439.822971502571)

    def test_perimeter_regular_2(self):
        res = circle.perimeter(100)
        self.assertAlmostEqual(res, 628.3185307179587)

    def test_perimeter_regular_3(self):
        res = circle.perimeter(3)
        self.assertAlmostEqual(res, 18.84955592153876)

    # tests with long numbers

    def test_perimeter_long_1(self):
        res = circle.perimeter(123456789000)
        self.assertAlmostEqual(res, 775701882716.3704)

    def test_perimeter_long_2(self):
        res = circle.perimeter(10973936690260632)
        self.assertAlmostEqual(res, 6.8951277774164584e+16)

    def test_perimeter_long_3(self):
        res = circle.perimeter(123456789)
        self.assertAlmostEqual(res, 775701882.7163703)


# class with test for funcs from file "square.py"


class SquareTestCase(unittest.TestCase):
    # tests with zero result

    def test_area_zero_1(self):
        res = square.area(0)
        self.assertEqual(res, "inappropriate input parameters")

    # tests with float result

    def test_area_float_1(self):
        res = square.area(1.10101)
        self.assertEqual(res, 1.2122230201000002, DELTA)

    # tests with negative parameter

    def test_area_negative_1(self):
        res = square.area(-100000)
        self.assertEqual(res, "inappropriate input parameters")

    def test_area_negative_2(self):
        res = square.area(-1)
        self.assertEqual(res, "inappropriate input parameters")

    # tests with regular numbers

    def test_area_regular_1(self):
        res = square.area(23)
        self.assertEqual(res, 529)

    def test_small_numbers_area_regular_2(self):
        res = square.area(100)
        self.assertEqual(res, 10000)

    def test_area_3(self):
        res = square.area(3)
        self.assertEqual(res, 9)

    # tests with long numbers

    def test_area_long_1(self):
        res = square.area(123456789000)
        self.assertEqual(res, 15241578750190521000000)

    def test_area_long_2(self):
        res = square.area(10973936690260632)
        self.assertEqual(res, 120427286481848474234844089039424)

    def test_area_long_3(self):
        res = square.area(1000000000)
        self.assertEqual(res, 1000000000000000000)

    # tests with zero result

    def test_perimeter_zero_1(self):
        res = square.perimeter(0)
        self.assertEqual(res, "inappropriate input parameters")

    # tests with float result

    def test_perimeter_float_1(self):
        res = square.perimeter(1.101067678981)
        self.assertEqual(res, 4.404270715924, DELTA)

    # tests with negative parameter

    def test_perimeter_negative_1(self):
        res = square.perimeter(-100000)
        self.assertEqual(res, "inappropriate input parameters")

    def test_perimeter_negative_2(self):
        res = square.perimeter(-1)
        self.assertEqual(res, "inappropriate input parameters")

    # tests with regular numbers

    def test_perimeter_regular_1(self):
        res = square.perimeter(70)
        self.assertEqual(res, 280)

    def test_perimeter_regular_2(self):
        res = square.perimeter(100)
        self.assertEqual(res, 400)

    def test_perimeter_regular_3(self):
        res = square.perimeter(3)
        self.assertEqual(res, 12)

    # tests with long numbers

    def test_perimeter_long_1(self):
        res = square.perimeter(123456789000)
        self.assertEqual(res, 493827156000)

    def test_perimeter_long_2(self):
        res = square.perimeter(10973936690260632)
        self.assertEqual(res, 43895746761042528)

    def test_perimeter_long_3(self):
        res = square.perimeter(1234567893984385555555)
        self.assertEqual(res, 4938271575937542222220)


# class with test for funcs from file "triangle.py"


class TriangleTestCase(unittest.TestCase):
    # tests with zero result

    def test_area_zero_1(self):
        res = triangle.area(12, 0)
        self.assertEqual(res, "inappropriate input parameters")

    def test_area_zero_2(self):
        res = triangle.area(0, 21)
        self.assertEqual(res, "inappropriate input parameters")

    def test_area_zero_3(self):
        res = triangle.area(0, 0)
        self.assertEqual(res, "inappropriate input parameters")

    # tests with float result

    def test_area_float_1(self):
        res = triangle.area(1.10101, 1.8)
        self.assertEqual(res, 0.990909, DELTA)

    # tests with negative parameter
    def test_area_negative_1(self):
        res = triangle.area(-12, 6)
        self.assertEqual(res, "inappropriate input parameters")

    def test_area_negative_2(self):
        res = triangle.area(4, -21)
        self.assertEqual(res, "inappropriate input parameters")

    # tests with regular numbers

    def test_area_regular_1(self):
        res = triangle.area(23, 2)
        self.assertEqual(res, 23)

    def test_area_regular_2(self):
        res = triangle.area(100, 5)
        self.assertEqual(res, 250)

    def test_area_regular_3(self):
        res = triangle.area(3, 3)
        self.assertEqual(res, 4.5)

    # tests with long numbers

    def test_area_long_1(self):
        res = triangle.area(123456789, 88888888)
        self.assertEqual(res, 5486968345130316.0)

    def test_area_long_2(self):
        res = triangle.area(10973936690260632, 2)
        self.assertEqual(res, 10973936690260632.0)

    def test_area_long_3(self):
        res = triangle.area(123456789, 21947873380521264)
        self.assertEqual(res, 1.3548069864688651e+24)

    # tests with zero result

    def test_perimeter_zero_1(self):
        res = triangle.perimeter(0, 0, 0)
        self.assertEqual(res, "inappropriate input parameters")

    def test_perimeter_zero_2(self):
        res = triangle.perimeter(3, 0, 3)
        self.assertEqual(res, "inappropriate input parameters")

    def test_perimeter_zero_3(self):
        res = triangle.perimeter(0, 3, 0)
        self.assertEqual(res, "inappropriate input parameters")

    # tests with float result

    def test_perimeter_float_1(self):
        res = triangle.perimeter(1.10101, 1.8, 456.7890)
        self.assertEqual(res, 459.69001, DELTA)

    # tests with negative parameter

    def test_perimeter_negative_1(self):
        res = triangle.perimeter(-100000, 1, 4)
        self.assertEqual(res, "inappropriate input parameters")

    def test_perimeter_negative_2(self):
        res = triangle.perimeter(-1, 5, 7)
        self.assertEqual(res, "inappropriate input parameters")

    def test_perimeter_negative_3(self):
        res = triangle.perimeter(-1, 5, -6)
        self.assertEqual(res, "inappropriate input parameters")

    # tests with regular numbers

    def test_perimeter_regular_1(self):
        res = triangle.perimeter(39, 2, 40)
        self.assertEqual(res, 81)

    def test_perimeter_regular_2(self):
        res = triangle.perimeter(60, 25, 50)
        self.assertEqual(res, 135)

    def test_perimeter_regular_3(self):
        res = triangle.perimeter(3, 3, 4)
        self.assertEqual(res, 10)

    # tests with long numbers

    def test_perimeter_long_1(self):
        res = triangle.perimeter(123456789000, 88888888000, 34567901019)
        self.assertEqual(res, 246913578019)

    def test_perimeter_long_2(self):
        res = triangle.perimeter(10973936690260632, 2, 10973936690260631)
        self.assertEqual(res, 21947873380521265)

    def test_perimeter_long_3(self):
        res = triangle.perimeter(123456789, 21947873380521264, 21947873257064480)
        self.assertEqual(res, 43895746761042533)


if __name__ == '__main__':
    unittest.main()
