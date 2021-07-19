import figure


class Square(figure.Figure):
    _name = "Square"

    def __new__(cls, line1):
        if line1 > 0:
            return super().__new__(cls)
        else:
            return None

    @property
    def area(self):
        return self.line1_length ** 2

    @property
    def perimeter(self):
        return 4 * self.line1_length
