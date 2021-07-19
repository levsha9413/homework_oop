from math import sqrt, pi


class Figure:
    _name = None

    def __init__(self, line_lenght):
        self.line1_length = line_lenght

    def add_area(self, figure_x):
        if not issubclass(type(figure_x), Figure):
            raise ValueError(f"{figure_x} is Class {type(figure_x)}. Is not a figure.")
        return self.area + figure_x.area

    @property
    def area(self):
        return None

    @property
    def perimeter(self):
        return None

    @property
    def name(self):
        return self._name
