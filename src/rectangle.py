import figure


class Rectangle(figure.Figure):
    _name = "Rectangle"

    def __new__(cls, line1, line2):
        if line1 > 0 and line2 > 0:
            return super().__new__(cls)
        else:
            return None

    def __init__(self, line1, line2):
        super().__init__(line1)
        self.line2_length = line2

    @property
    def area(self):
        return self.line1_length * self.line2_length

    @property
    def perimeter(self):
        return 2 * (self.line2_length + self.line1_length)
