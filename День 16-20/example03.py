"""
Рекурсивный вызов функции - функция вызывает себя прямо или косвенно
1. Условия сходимости
2. Рекурсивная формула
п! = п * (п-1)!
е (п) = е (п-1) + е (п-2)
1 1 2 3 5 8 13 21 34 55 ...
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
    # for val in fib3(20):
    #     print(val)
    # gen = fib3(20)
    # for _ in range(10):
    #     print(next(gen))
    for num in range(1, 121):
        with timer():
            print(f'{num}: {fib(num)}')
    # print(fac(5))
    # print(fac(-5))


if __name__ == '__main__':
    main()
