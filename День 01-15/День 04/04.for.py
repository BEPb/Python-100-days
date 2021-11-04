"""
Введите положительное целое число, чтобы определить, является ли оно простым.
Название файла '04.for.py'

Version: 0.1
Author: Andrej Marinchenko
Date: 2021-11-04
"""

from math import sqrt

num = int(input('Пожалуйста, введите положительное целое число: '))
end = int(sqrt(num))
is_prime = True
for x in range(2, end + 1):
    if num % x == 0:
        is_prime = False
        break
if is_prime and num != 1:
    print('%d - простое число' % num)
else:
    print('%d - не является простым числом' % num)
