"""
Последовательность Фибоначчи - используя ключевое слово yield
Python 3.10 генератор синтаксис
Название файла '18.Фибоначчи.py'

Version: 0.1
Author: Andrej Marinchenko
Date: 2023-04-10
"""


def fib(num):
    n, a, b = 0, 0, 1
    while n < num:
        yield b
        a, b = b, a + b
        n += 1


for x in fib(20):
    print(x)
