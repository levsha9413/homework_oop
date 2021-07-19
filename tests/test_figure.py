import pytest
from src.figure import Figure

''' Запретить создавать экземпляры базового класса Figure'''
'''
def test_figure_created():
    with pytest.raises(Exception):
        Figure(1)
'''
def test_a():
    print(Figure())