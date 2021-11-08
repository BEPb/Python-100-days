"""
Python 3.9 Применение метода экземпляра и метода класса
Название файла '10.метод_экземпляра.py'

Version: 0.1
Author: Andrej Marinchenko
Date: 2021-11-09
"""

from math import sqrt


class Triangle(object):

    def __init__(self, a, b, c):
        self._a = a
        self._b = b
        self._c = c

    # Статический метод
    @staticmethod
    def is_valid(a, b, c):
        return a + b > c and b + c > a and c + a > b

    # Пример метода
    def perimeter(self):
        return self._a + self._b + self._c

    # Пример метода
    def area(self):
        p = self.perimeter() / 2
        return sqrt(p * (p - self._a) * (p - self._b) * (p - self._c))


if __name__ == '__main__':
    # Используйте метод разделения строки, чтобы разбить строку на список
    # Затем используйте функцию карты, чтобы сопоставить каждую строку в списке с десятичными знаками
    a, b, c = map(float, input('Укажите три стороны: ').split())
    # Сначала решите, могут ли три стороны заданной длины образовывать треугольник
    # Создайте объект треугольник, если это возможно
    if Triangle.is_valid(a, b, c):
        tri = Triangle(a, b, c)
        print('Периметр:', tri.perimeter())
        print('Площадь:', tri.area())
        # Если вы передаете объект в качестве параметра метода, вы также можете вызвать метод экземпляра через класс
        # print('Периметр:', Triangle.perimeter(tri))
        # print('Площадь:', Triangle.area(tri))
        # Посмотрите на приведенный ниже код, чтобы понять, что это одно и то же
        # print(type(tri.perimeter))
        # print(type(Triangle.perimeter))
    else:
        print('Не получается треугольник.')
