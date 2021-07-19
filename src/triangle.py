from src.figure import Figure
from math import sqrt


class Triangle(Figure):
    _name = "Triangle"

    def __new__(cls, line1, line2, line3):
        if line1 > 0 and line2 > 0 and line3 > 0 and line1 + line2 > line3 and line1 + line3 > line2 and \
                line2 + line3 > line1:
            return super().__new__(cls)
        else:
            return None

    def __init__(self, line1, line2, line3):
        super().__init__(line1)
        self.line2_length = line2
        self.line3_length = line3

    @property
    def area(self):
        p = self.perimeter / 2
        return sqrt(p * (p - self.line3_length) * (p - self.line2_length) * (p - self.line3_length))

    @property
    def perimeter(self):
        return self.line3_length + self.line2_length + self.line1_length
