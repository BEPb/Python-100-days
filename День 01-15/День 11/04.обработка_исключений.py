"""
Python 3.10 Выбрасывать исключения в стек исключений
Название файла '04.обработка_исключений.py'

Version: 0.1
Author: Andrej Marinchenko
Date: 2023-04-09
"""


def f1():
    raise AssertionError('Произошло исключение')


def f2():
    f1()


def f3():
    f2()


f3()
