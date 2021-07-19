from math import pi
from src.figure import Figure


class Circle(Figure):
    _name = "Circle"

    def __new__(cls, radius):
        if radius > 0:
            return super().__new__(cls)
        else:
            return None

    def __init__(self, radius):
        self.radius = radius

    @property
    def area(self):
        return (self.radius ** 2) * pi

    @property
    def perimeter(self):
        return self.radius * 2 * pi
