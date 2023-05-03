"""
Python 3.10 Область действия переменных и порядок, в котором Python ищет переменные
Название файла '03.область_действия.py'

Version: 0.1
Author: Andrej Marinchenko
Date: 2023-05-03
"""
x = 100


def foo():
    global x
    x = 200

    def bar():
        x = 300
        print(x)

    bar()
    print(x)


foo()
print(x)
