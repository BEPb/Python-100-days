"""
Python 3.9  Перегрузка оператора - настраиваемый класс оценки
Название файла '08.перегрузка_оператора.py'

Version: 0.1
Author: Andrej Marinchenko
Date: 2021-11-09
"""

from math import gcd  # импорт вызова факториала


class Rational(object):  # определяем класс

    def __init__(self, num, den=1):  # инициализируем класс (на входе 2 аргумента, один из них по умолчанию равен 1)
        if den == 0:  # если аргумент = 0
            raise ValueError('Знаменатель не может быть 0')  # то вывод предупреждения
        self._num = num  # присваиваем атрибуту значение аргумента
        self._den = den  # присваиваем атрибуту значение аргумента
        self.normalize()  # вызываем метод

    def simplify(self):  # метод математических операций
        x = abs(self._num)
        y = abs(self._den)
        factor = gcd(x, y)
        if factor > 1:
            self._num //= factor
            self._den //= factor
        return self

    def normalize(self):  # метод смены знака, если он отрицательный
        if self._den < 0:
            self._den = -self._den
            self._num = -self._num
        return self

    def __add__(self, other):  # метод сложения объектов
        new_num = self._num * other._den + other._num * self._den
        new_den = self._den * other._den
        return Rational(new_num, new_den).simplify().normalize()

    def __sub__(self, other):  # метод вычитания объектов
        new_num = self._num * other._den - other._num * self._den
        new_den = self._den * other._den
        return Rational(new_num, new_den).simplify().normalize()

    def __mul__(self, other):  # метод умножения объектов
        new_num = self._num * other._num
        new_den = self._den * other._den
        return Rational(new_num, new_den).simplify().normalize()

    def __truediv__(self, other):  # метод деления объектов
        new_num = self._num * other._den
        new_den = self._den * other._num
        return Rational(new_num, new_den).simplify().normalize()

    def __str__(self):  # метод строчного представления
        if self._num == 0:
            return '0'
        elif self._den == 1:
            return str(self._num)
        else:
            return '(%d/%d)' % (self._num, self._den)


if __name__ == '__main__':  # если программа запущена как главная
    r1 = Rational(2, 3)  # создаем объект
    print(r1)  # выводим значения объекта
    r2 = Rational(6, -8)  # создаем объект
    print(r2)  # выводим значения объекта
    print(r2.simplify())  # вызываем метод матем. операций
    print('%s + %s = %s' % (r1, r2, r1 + r2))
    print('%s - %s = %s' % (r1, r2, r1 - r2))
    print('%s * %s = %s' % (r1, r2, r1 * r2))
    print('%s / %s = %s' % (r1, r2, r1 / r2))
