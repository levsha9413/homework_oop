import pytest
import src.triangle
import src.square
import src.circle
import src.rectangle
import src.figure


# Создать дефолтные фигуры для операций


# Triangle
@pytest.fixture(scope="session")
def default_triangle(request):
    def_triangle = src.triangle.Triangle(3, 3, 3)

    yield def_triangle
    del def_triangle


# Rectangle
@pytest.fixture(scope="session")
def default_rectangle(request):
    def_rectangle = src.rectangle.Rectangle(3, 3)

    yield def_rectangle
    del def_rectangle


# Square
@pytest.fixture(scope="session")
def default_square(request):
    def_square = src.square.Square(3)

    yield def_square
    del def_square


# Circle
@pytest.fixture(scope="session")
def default_circle(request):
    def_circle = src.circle.Circle(3)

    yield def_circle
    del def_circle
