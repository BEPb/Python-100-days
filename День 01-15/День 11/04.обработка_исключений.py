"""
Python 3.9 Выбрасывать исключения в стек исключений
Название файла '04.обработка_исключений.py'

Version: 0.1
Author: Andrej Marinchenko
Date: 2021-11-11
"""


def f1():
    raise AssertionError('Произошло исключение')


def f2():
    f1()


def f3():
    f2()


f3()
