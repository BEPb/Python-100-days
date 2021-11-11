"""
Python 3.9 Написать текстовый файл
Записать в файл простые числа в пределах 100
Название файла '01.Связь_между_объектами.py'

Version: 0.1
Author: Andrej Marinchenko
Date: 2021-11-11
"""

from math import sqrt


def is_prime(n):
    for factor in range(2, int(sqrt(n)) + 1):
        if n % factor == 0:
            return False
    return True



with open('prime.txt', 'w') as f:
    for num in range(2, 100):
        if is_prime(num):
            f.write(str(num) + '\n')
print('Запись завершена!')
