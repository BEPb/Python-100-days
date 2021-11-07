"""
Python 3.9 Определите и используйте класс прямоугольника
Название файла '04.прямоугольник.py'

Version: 0.1
Author: Andrej Marinchenko
Date: 2021-11-08
"""


class Rect(object):
    """Класс прямоугольника"""

    def __init__(self, width=0, height=0):
        """Метод инициализации"""
        self.__width = width
        self.__height = height

    def perimeter(self):
        """Рассчитать периметр"""
        return (self.__width + self.__height) * 2

    def area(self):
        """Рассчитать площадь"""
        return self.__width * self.__height

    def __str__(self):
        """Строковое выражение объекта Rectangle"""
        return '矩形[%f,%f]' % (self.__width, self.__height)

    def __del__(self):
        """Анализатор"""
        print('Уничтожить прямоугольный объект')


if __name__ == '__main__':
    rect1 = Rect()
    print(rect1)
    print(rect1.perimeter())
    print(rect1.area())
    rect2 = Rect(3.5, 4.5)
    print(rect2)
    print(rect2.perimeter())
    print(rect2.area())
