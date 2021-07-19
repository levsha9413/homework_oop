import pytest
from src.figure import Figure


def test_figure_created():
    ''' Запретить создавать экземпляры базового класса Figure'''
    with pytest.raises(Exception):
        Figure(1)
