"""
Python 3.10 Магический метод Итератор
Название файла 'example01.py'

Version: 0.1
Author: Andrej Marinchenko
Date: 2023-05-05
"""

class MyIterator:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def __iter__(self):
        return self

    def __next__(self):
        if self.start >= self.end:
            raise StopIteration
        else:
            self.start += 1
            return self.start - 1


def main():
    numbers = MyIterator(0, 5)
    for number in numbers:
        print(number)


if __name__ == '__main__':
    main()

