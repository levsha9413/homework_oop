import pytest
from src.figure import Figure
from src.triangle import Triangle


def test_create_triangle():
    '''Проверка возможности создания треугольника '''

    t = Triangle(10, 11, 12)
    assert (t != None)


def test_default_triangle(default_triangle):
    '''Верификация по полям дефолтного объекта из conftest, используемого в последующих тестах '''
    t = Triangle(3, 3, 3)
    assert (dir(t) == dir(default_triangle))


def test_attributes(default_triangle):
    '''Объект создается с необходимыми атрибутами и методами'''
    assert (dir(default_triangle) == ['__class__',
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
                                      'line3_length',
                                      'name',
                                      'perimeter'])


def test_name(default_triangle):
    '''Объект имеет атрибут name c правильным значением'''
    assert (default_triangle.name == "Triangle")


def test_is_figure(default_triangle):
    '''Класс унаследован от Figure '''
    assert issubclass(type(default_triangle), Figure)


def test_area(default_triangle):
    '''Проверка атрибута area'''
    assert (default_triangle.area == 3.897114317029974)


def test_perimeter_first(default_triangle):
    '''Провверка атрибута perimeter'''
    assert (default_triangle.perimeter == 9)


def test_perimeter_second():
    '''Провверка метода perimeter c другими данными'''
    assert (Triangle(10, 11, 12).perimeter == 33)


def test_add_area(default_triangle):
    '''Проверка метода add_area'''
    assert (default_triangle.add_area(default_triangle) == 7.794228634059948)


def test_add_area_two(default_triangle):
    '''Проверка метода add_area c объектами разной площади'''
    a = Triangle(10, 7, 14)
    assert (default_triangle.add_area(a) == 21.114474741903468)


def test_add_area_value_error(default_triangle):
    '''Если передана не геометрическая фигура, то нужно выбрасывать ошибку (raise ValueError)'''
    with pytest.raises(ValueError):
        default_triangle.add_area(1)


'''

Требование: При невозможности создать треугольник, возвращается None

Проверки с 0 в аргументах:

'''


def test_zero_argument_first():
    assert (Triangle(0, 3, 3) == None)


def test_zero_argument_second():
    assert (Triangle(3, 0, 3) == None)


def test_zero_argument_third():
    assert (Triangle(3, 3, 0) == None)


def test_zero_argument_fourth():
    assert (Triangle(0, 0, 0) == None)


'''

Проверки с отрицательными аргументами:

'''


def test_negative_argument_first():
    assert (Triangle(-3, 3, 3) == None)


def test_negative_argument_second():
    assert (Triangle(3, -3, 3) == None)


def test_negative_argument_third():
    assert (Triangle(3, 3, -3) == None)


def test_negative_argument_fourth():
    assert (Triangle(-3, -3, -3) == None)


def test_deficiency_arguments():
    '''Проверка с недостаточным количеством аргументов'''
    with pytest.raises(TypeError):
        Triangle(1, 2)


'''
Проверки геометрически невозможных треугольников:
'''


def test_geometric_a():
    assert (Triangle(3, 3, 6) == None)


def test_geometric_b():
    assert (Triangle(6, 3, 3) == None)


def test_geometric_c():
    assert (Triangle(3, 6, 3) == None)
