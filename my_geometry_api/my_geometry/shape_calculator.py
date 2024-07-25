from my_geometry_api.my_geometry import Circle, Triangle


class ShapeAreaCalculator:
    def __init__(self):
        self.circle = Circle()
        self.triangle = Triangle()

    def calculate_area(self, shape_type, *args):
        if shape_type == 'circle':
            if len(args) != 1:
                raise ValueError("Для вычисления площади круга требуется ровно один аргумент (радиус)")
            return self.circle.area(*args)
        elif shape_type == 'triangle':
            if len(args) != 3:
                raise ValueError("Для вычисления площади треугольника требуется ровно три аргумента (сторона1, сторона2, сторона3)")
            return self.triangle.area(*args)
        else:
            raise ValueError("Неподдерживаемый тип фигуры")

    def is_right_triangle(self, *args):
        if len(args) != 3:
            raise ValueError("Для проверки треугольника требуется ровно три аргумента (сторона1, сторона2, сторона3)")
        return self.triangle.is_right_triangle(*args)