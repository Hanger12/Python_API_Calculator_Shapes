import math


class Triangle:
    def area(self, side1, side2, side3):
        s = (side1 + side2 + side3) / 2
        area = math.sqrt(s * (s - side1) * (s - side2) * (s - side3))
        return area

    def is_right_triangle(self, side1, side2, side3):
        sides = [side1, side2, side3]
        sides.sort()
        return sides[0] ** 2 + sides[1] ** 2 == sides[2] ** 2