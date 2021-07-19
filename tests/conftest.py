import pytest
import src.triangle
import src.square
import src.circle
import src.rectangle


# Создать дефолтные фигуры для операций


# Triangle
@pytest.fixture(scope="session")
def default_triangle(request):
    def_triangle = src.triangle.Triangle(3, 3, 3)

    def final():
        del def_triangle

    request.addfinalizer(final)

    return def_triangle


# Rectangle
@pytest.fixture(scope="session")
def default_rectangle(request):
    def_rectangle = src.rectangle.Rectangle(3, 3)

    def final():
        del def_rectangle

    request.addfinalizer(final)

    return def_rectangle


# Square
@pytest.fixture(scope="session")
def default_square(request):
    def_square = src.square.Square(3)

    def final():
        del def_square

    request.addfinalizer(final)

    return def_square


# Circle
@pytest.fixture(scope="session")
def default_circle(request):
    def_circle = src.circle.Circle(3)

    def final():
        del def_circle

    request.addfinalizer(final)

    return def_circle
