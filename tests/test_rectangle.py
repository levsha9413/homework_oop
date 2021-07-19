import pytest
from src.figure import Figure
from src.rectangle import Rectangle


def test_create_rectangle():
    '''Проверка возможности создания '''

    t = Rectangle(10, 11)
    assert (t != None)


def test_default_rectangle(default_rectangle):
    '''Верификация по полям дефолтного объекта из conftest, используемого в последующих тестах '''
    t = Rectangle(3, 3)
    assert (dir(t) == dir(default_rectangle))


def test_attributes(default_rectangle):
    '''Объект создается с необходимыми атрибутами и методами'''
    assert (dir(default_rectangle) == ['__class__',
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
                                       'line1_length',
                                       'line2_length',
                                       'name',
                                       'perimeter'])


def test_name(default_rectangle):
    '''Объект имеет атрибут name c правильным значением'''
    assert (default_rectangle.name == "Rectangle")


def test_is_figure(default_rectangle):
    '''Класс унаследован от Figure '''
    assert issubclass(type(default_rectangle), Figure)


def test_area(default_rectangle):
    '''Проверка атрибута area'''
    assert (default_rectangle.area == 9)


def test_perimeter_first(default_rectangle):
    '''Провверка атрибута perimeter'''
    assert (default_rectangle.perimeter == 12)


def test_perimeter_second():
    '''Провверка метода perimeter c другими данными'''
    assert (Rectangle(10, 11).perimeter == 42)


def test_add_area(default_rectangle):
    '''Проверка метода add_area'''
    assert (default_rectangle.add_area(default_rectangle) == 18)


def test_add_area_two(default_rectangle):
    '''Проверка метода add_area c объектами разной площади'''
    a = Rectangle(10, 7)
    assert (default_rectangle.add_area(a) == 79)


def test_add_area_value_error(default_rectangle):
    '''Если передана не геометрическая фигура, то нужно выбрасывать ошибку (raise ValueError)'''
    with pytest.raises(ValueError):
        default_rectangle.add_area(1)


'''

Проверки с 0 в аргументах:

'''


def test_zero_argument_first():
    assert (Rectangle(0, 3) == None)


def test_zero_argument_second():
    assert (Rectangle(3, 0) == None)


def test_zero_argument_third():
    assert (Rectangle(0, 0) == None)


'''

Проверки с отрицательными аргументами:

'''


def test_negative_argument_first():
    assert (Rectangle(-3, 3) == None)


def test_negative_argument_second():
    assert (Rectangle(3, -3) == None)


def test_negative_argument_third():
    assert (Rectangle(-3, -3) == None)


def test_deficiency_arguments():
    '''Проверка с недостаточным количеством аргументов'''
    with pytest.raises(TypeError):
        Rectangle(1)
