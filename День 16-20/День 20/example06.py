"""
Python 3.10
Эта программа использует asyncio, чтобы запустить две асинхронные задачи для фильтрации простых чисел и создания
списка квадратов в заданном диапазоне чисел.
Название файла 'example06.py'

Version: 0.1
Author: Andrej Marinchenko
Date: 2023-05-13
"""
import asyncio
from example05 import is_prime  # Функция `is_prime(n)` используется для проверки, является ли число `n` простым числом


def num_generator(m, n):
    """Генератор чисел указанного диапазона
    Функция `num_generator(m, n)` генерирует числа в диапазоне от `m` до `n`, используя ключевое слово `yield from`.
    """
    yield from range(m, n + 1)


async def prime_filter(m, n):
    """
    Главный фильтр
    Функция `prime_filter(m, n)` использует функцию `num_generator(m, n)` для генерации чисел в заданном диапазоне.
    Затем она проверяет, является ли каждое число простым числом, используя функцию `is_prime(n)`. Если число является
    простым, оно добавляется в список `primes`. Функция `prime_filter(m, n)` также использует `await asyncio.sleep(
    0.001)` для имитации скорости работы.
    """
    primes = []
    for i in num_generator(m, n):
        if is_prime(i):
            print('Простое число =>', i)
            primes.append(i)

        await asyncio.sleep(0.001)
    return tuple(primes)


async def square_mapper(m, n):
    """Квадратный картограф
    Функция `square_mapper(m, n)` использует ту же функцию генератора чисел `num_generator(m, n)`, чтобы создать список
    квадратов каждого числа в диапазоне. Используется `await asyncio.sleep(0.001)` для имитации времени выполнения.
    """
    squares = []
    for i in num_generator(m, n):
        print('Квадрат числа =>', i * i)
        squares.append(i * i)

        await asyncio.sleep(0.001)
    return squares


def main():
    """Основная функция
    В основной функции `main()`, каждая задача выполняется в своей собственной корутине, а затем они объединяются в
    объект `gather`, чтобы выполняться одновременно.

    `future.add_done_callback(lambda x: print(x.result()))` используется для создания обратного вызова (callback),
    который вызывается, когда выполняется каждая задача. Результаты будут выведены на экран.

    В конце `loop.run_until_complete(future)` используется для запуска общей задачи и `loop.close()` закрывает цикл событий.
    Coroutine - кооперативная подпрограмма, которую можно переключать при необходимости
    """
    loop = asyncio.get_event_loop()
    future = asyncio.gather(prime_filter(2, 100), square_mapper(1, 100))
    future.add_done_callback(lambda x: print(x.result()))
    loop.run_until_complete(future)
    loop.close()


if __name__ == '__main__':
	main()