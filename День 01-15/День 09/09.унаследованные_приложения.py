"""
Python 3.9  Унаследованные приложения
-Абстрактный класс
-Абстрактный метод
-Метод переписывания
-Полиморфизм
Название файла '09.унаследованные_приложения.py'

Version: 0.1
Author: Andrej Marinchenko
Date: 2021-11-09
"""

from abc import ABCMeta, abstractmethod
from math import pi


class Shape(object, metaclass=ABCMeta):

    @abstractmethod
    def perimeter(self):
        pass

    @abstractmethod
    def area(self):
        pass


class Circle(Shape):

    def __init__(self, radius):
        self._radius = radius

    def perimeter(self):
        return 2 * pi * self._radius

    def area(self):
        return pi * self._radius ** 2

    def __str__(self):
        return 'я - круг'


class Rect(Shape):

    def __init__(self, width, height):
        self._width = width
        self._height = height

    def perimeter(self):
        return 2 * (self._width + self._height)

    def area(self):
        return self._width * self._height

    def __str__(self):
        return 'Я - прямоугольник'


if __name__ == '__main__':
    shapes = [Circle(5), Circle(3.2), Rect(3.2, 6.3)]
    for shape in shapes:
        print(shape)
        print('Периметр:', shape.perimeter())
        print('Площадь:', shape.area())
