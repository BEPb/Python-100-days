"""
Использование многопроцессного и технологического пула
Многопоточность не может использовать преимущества многоядерных характеристик ЦП из-за существования GIL
Для ресурсоемких задач следует учитывать многопроцессорность.
время python3 example22.py
реальный 0 мин. 11,512 сек.
пользователь 0m39.319s
sys 0m0.169s
"""
import concurrent.futures
import math

PRIMES = [
    1116281,
    1297337,
    104395303,
    472882027,
    533000389,
    817504243,
    982451653,
    112272535095293,
    112582705942171,
    112272535095293,
    115280095190773,
    115797848077099,
    1099726899285419
] * 5


def is_prime(n):
    """Оценка простых чисел"""
    if n % 2 == 0:
        return False

    sqrt_n = int(math.floor(math.sqrt(n)))
    for i in range(3, sqrt_n + 1, 2):
        if n % i == 0:
            return False
    return True


def main():
    """Основная функция"""
    with concurrent.futures.ProcessPoolExecutor() as executor:
        for number, prime in zip(PRIMES, executor.map(is_prime, PRIMES)):
            print('%d is prime: %s' % (number, prime))


if __name__ == '__main__':
    main()
