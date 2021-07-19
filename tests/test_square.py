import pytest
from src.figure import Figure
from src.square import Square


def test_create_square():
    '''Проверка возможности создания '''

    t = Square(10)
    assert (t != None)


def test_default_square(default_square):
    '''Верификация по полям дефолтного объекта из conftest, используемого в последующих тестах '''
    t = Square(3)
    assert (dir(t) == dir(default_square))


def test_attributes(default_square):
    '''Объект создается с необходимыми атрибутами и методами'''
    assert (dir(default_square) == ['__class__',
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
                                    'name',
                                    'perimeter'])


def test_name(default_square):
    '''Объект имеет атрибут name c правильным значением'''
    assert (default_square.name == "Square")


def test_is_figure(default_square):
    '''Класс унаследован от Figure '''
    assert issubclass(type(default_square), Figure)


def test_area(default_square):
    '''Проверка атрибута area'''
    assert (default_square.area == 9)


def test_perimeter_first(default_square):
    '''Провверка атрибута perimeter'''
    assert (default_square.perimeter == 12)


def test_perimeter_second():
    '''Провверка метода perimeter c другими данными'''
    assert (Square(10).perimeter == 40)


def test_add_area(default_square):
    '''Проверка метода add_area'''
    assert (default_square.add_area(default_square) == 18)


def test_add_area_two(default_square):
    '''Проверка метода add_area c объектами разной площади'''
    a = Square(7)
    assert (default_square.add_area(a) == 58)


def test_add_area_value_error(default_square):
    '''Если передана не геометрическая фигура, то нужно выбрасывать ошибку (raise ValueError)'''
    with pytest.raises(ValueError):
        default_square.add_area(1)


def test_zero_argument():
    ''' Проверка  0 в аргументах '''
    assert (Square(0) == None)


def test_negative_argument_first():
    ''' Проверка с отрицательным аргументом: '''
    assert (Square(-3) == None)


def test_deficiency_arguments():
    '''Проверка с недостаточным количеством аргументов'''
    with pytest.raises(TypeError):
        Square()
