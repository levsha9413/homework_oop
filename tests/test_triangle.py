import pytest

from src.triangle import Triangle

'''Дописать тест что класс триугольник унаследован от класса фигур '''

def is_figure(triangle):
    assert issubclass(Triangle, Figure)
