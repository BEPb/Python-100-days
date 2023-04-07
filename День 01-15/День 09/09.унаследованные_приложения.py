"""
Python 3.10  Унаследованные приложения
-Абстрактный класс
-Абстрактный метод
-Метод переписывания
-Полиморфизм
Название файла '09.унаследованные_приложения.py'

Version: 0.1
Author: Andrej Marinchenko
Date: 2023-04-07
"""

from abc import ABCMeta, abstractmethod  # импорт метаобъектов и абстрактных классов
from math import pi  # импорт константы пи


class Shape(object, metaclass=ABCMeta):  # создаем класс унаследованный от метакласса

    @abstractmethod  # свойство периметр
    def perimeter(self):
        pass  # пустой

    @abstractmethod  # свойство площадь
    def area(self):
        pass  # пустой


class Circle(Shape):  # создаем класс унаследованный от класса Shape

    def __init__(self, radius):  # инициализация класса
        self._radius = radius

    def perimeter(self):  # метод периметра
        return 2 * pi * self._radius

    def area(self):  # метод площади
        return pi * self._radius ** 2

    def __str__(self):  # метод строчного представления при вызове объекта
        return 'я - круг'


class Rect(Shape):  # создаем класс унаследованный от класса Shape

    def __init__(self, width, height):  # инициализация класса
        self._width = width
        self._height = height

    def perimeter(self):  # метод периметра
        return 2 * (self._width + self._height)

    def area(self):  # метод площади
        return self._width * self._height

    def __str__(self):  # метод строчного представления при вызове объекта
        return 'Я - прямоугольник'


if __name__ == '__main__':  # если программа запущена как главная
    shapes = [Circle(5), Circle(3.2), Rect(3.2, 6.3)]  # создаем список объектов
    for shape in shapes:  # перебираем объекты по списку
        print(shape)  # выводим информацию о объекте
        print('Периметр:', shape.perimeter())  # выводим информацию о периметре
        print('Площадь:', shape.area())  # выводим информацию о площади
