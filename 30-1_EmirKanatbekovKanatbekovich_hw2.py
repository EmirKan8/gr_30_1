import math


class Figure:
    unit = "cm"

    def __init__(self):
        pass

    def calculate_area(self):
        pass

    def info(self):
        pass


class Circle(Figure):
    def __init__(self, radius):
        self.__radius = radius

    def calculate_area(self):
        return round(math.pi * (self.__radius ** 2), 2)

    def info(self):
        print(f"Circle radius: {self.__radius}{Figure.unit}, area: {self.calculate_area()}{Figure.unit}.")


class RightTriangle(Figure):
    def __init__(self, side_a, side_b):
        self.__side_a = side_a
        self.__side_b = side_b

    def calculate_area(self):
        return round((self.__side_a * self.__side_b) / 2, 2)

    def info(self):
        print(
            f"RightTriangle side a: {self.__side_a}{Figure.unit}, side b: {self.__side_b}{Figure.unit}, area: {self.calculate_area()}{Figure.unit}.")


circle_1 = Circle(2)
circle_2 = Circle(3)

triangle_1 = RightTriangle(5, 10)
triangle_2 = RightTriangle(3, 7)
triangle_3 = RightTriangle(8, 12)

figures_list = [circle_1, circle_2, triangle_1, triangle_2, triangle_3]

for figure in figures_list:
    figure.info()

