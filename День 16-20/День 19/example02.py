"""
Python 3.10 Итератор - ряд Фибоначчи
Название файла 'example02.py'

Version: 0.1
Author: Andrej Marinchenko
Date: 2023-05-05
"""


class Fib(object):
    """Ряд Фибоначчи"""

    def __init__(self, num):
        self.num = num
        self.a, self.b = 0, 1
        self.idx = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.idx < self.num:
            self.a, self.b = self.b, self.a + self.b
            self.idx += 1
            return self.a
        raise StopIteration()


def main():
    numbers = Fib(5)
    for number in numbers:
        print(number)


if __name__ == '__main__':
    main()

