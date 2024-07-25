import math
import unittest

from my_geometry_api.calculate_shapes import ShapeAreaCalculator


class TestShapeAreaCalculator(unittest.TestCase):
    def setUp(self):
        self.calculator = ShapeAreaCalculator()

    def test_circle_area(self):
        self.assertAlmostEqual(self.calculator.calculate_area('circle', 3), math.pi * 9)

    def test_triangle_area(self):
        self.assertAlmostEqual(self.calculator.calculate_area('triangle', 3, 4, 5), 6)

    def test_is_right_triangle(self):
        self.assertTrue(self.calculator.is_right_triangle(3, 4, 5))
        self.assertFalse(self.calculator.is_right_triangle(5, 6, 7))


if __name__ == '__main__':
    unittest.main()
