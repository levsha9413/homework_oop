import pytest
from src.figure import Figure
from src.circle import Circle


def test_create_circle():
    '''Проверка возможности создания '''
    t = Circle(10)
    assert (t != None)


def test_default_circle(default_circle):
    '''Верификация по полям дефолтного объекта из conftest, используемого в последующих тестах '''
    t = Circle(3)
    assert (dir(t) == dir(default_circle))


def test_attributes(default_circle):
    '''Объект создается с необходимыми атрибутами и методами'''
    assert (dir(default_circle) == ['__class__',
                                    '__delattr__',
                                    '__dict__',
                                    '__dir__',
                                    '__doc__',
                                    '__eq__',
                                    '__format__',
                                    '__ge__',
                                    '__getattribute__',
                                    '__gt__',
                                    '__hash__',
                                    '__init__',
                                    '__init_subclass__',
                                    '__le__',
                                    '__lt__',
                                    '__module__',
                                    '__ne__',
                                    '__new__',
                                    '__reduce__',
                                    '__reduce_ex__',
                                    '__repr__',
                                    '__setattr__',
                                    '__sizeof__',
                                    '__str__',
                                    '__subclasshook__',
                                    '__weakref__',
                                    '_name',
                                    'add_area',
                                    'area',
                                    'name',
                                    'perimeter',
                                    'radius'])


def test_name(default_circle):
    '''Объект имеет атрибут name c правильным значением'''
    assert (default_circle.name == "Circle")


def test_is_figure(default_circle):
    '''Класс унаследован от Figure '''
    assert issubclass(type(default_circle), Figure)


def test_area(default_circle):
    '''Проверка атрибута area'''
    assert (default_circle.area == 28.274333882308138)


def test_perimeter_first(default_circle):
    '''Провверка атрибута perimeter'''
    assert (default_circle.perimeter == 18.84955592153876)


def test_perimeter_second():
    '''Провверка метода perimeter c другими данными'''
    assert (Circle(10).perimeter == 62.83185307179586)


def test_add_area(default_circle):
    '''Проверка метода add_area'''
    assert (default_circle.add_area(default_circle) == 56.548667764616276)


def test_add_area_two(default_circle):
    '''Проверка метода add_area c объектами разной площади'''
    a = Circle(7)
    assert (default_circle.add_area(a) == 182.21237390820798)


def test_add_area_value_error(default_circle):
    '''Если передана не геометрическая фигура, то нужно выбрасывать ошибку (raise ValueError)'''
    with pytest.raises(ValueError):
        default_circle.add_area(1)


def test_zero_argument():
    ''' Проверка  0 в аргументах '''
    assert (Circle(0) == None)


def test_negative_argument_first():
    ''' Проверка с отрицательным аргументом: '''
    assert (Circle(-3) == None)


def test_deficiency_arguments():
    '''Проверка с недостаточным количеством аргументов'''
    with pytest.raises(TypeError):
        Circle()
