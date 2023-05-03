"""
Python 3.10 Рекурсивный вызов функции - функция вызывает себя прямо или косвенно
1. Условия сходимости
2. Рекурсивная формула
п! = п * (п-1)!
е (п) = е (п-1) + е (п-2)
1 1 2 3 5 8 13 21 34 55 ...
Название файла '02.рекурсивная_функция.py'

Version: 0.1
Author: Andrej Marinchenko
Date: 2023-05-03
"""
from contextlib import contextmanager
from time import perf_counter


def fac(num):
    """Найдите факториал"""
    assert num >= 0
    if num in (0, 1):
        return 1
    return num * fac(num - 1)


def fib2(num):
    """Общая функция"""
    a, b = 1, 1
    for _ in range(num - 1):
        a, b = b, a + b
    return a


def fib3(num):
    """Строитель"""
    a, b = 0, 1
    for _ in range(num):
        a, b = b, a + b
        yield a


# Динамическое планирование - сохранение промежуточных результатов, которые могут быть повторены операциями (место для времени)
def fib(num, results={}):
    """Число Фибоначчи"""
    assert num > 0
    if num in (1, 2):
        return 1
    try:
        return results[num]
    except KeyError:
        results[num] = fib(num - 1) + fib(num - 2)
        return results[num]


@contextmanager
def timer():
    try:
        start = perf_counter()
        yield
    finally:
        end = perf_counter()
        print(f'{end - start}секунд')


def main():
    """Основная функция"""
    for val in fib3(20):  # этот цикл высчитывает и выводит первых 20 значений последовательности Фибоначчи
        print(val)  # выводит значение ряда Фибоначчи
    gen = fib3(20)  # генератор первых 20 чисел ряда Фибоначчи
    print(gen)  # <generator object fib3 at 0x0000027BFE782180>

    for _ in range(10):  # этот цикл получает значения от 0 до 9 на входе, на выходе 10 первых чисел ряда Фибоначи
        print(next(gen))  # используя генератор мы получаем конкретный элемент ряда Фибоначчи

    for num in range(1, 121):
        ''' этот цикл высчитывает значения первых 120 значений ряда Фибоначчи и выводит время 
        вычисления каждого числа ряда'''
        with timer():
            print(f'{num}: {fib(num)}')

    print(fac(5))  # 120
    print(fac(-5))  # выдаст ошибку AssertionError т.к. не выполняется условие num >= 0


if __name__ == '__main__':
    main()
