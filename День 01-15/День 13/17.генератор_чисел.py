"""
Python 3.10 генератор синтаксис
Название файла '17.генератор_чисел.py'

Version: 0.1
Author: Andrej Marinchenko
Date: 2023-04-10
"""

seq = [x * x for x in range(10)]
print(seq)

gen = (x * x for x in range(10))
print(gen)
for x in gen:
    print(x)

num = 10
gen = (x ** y for x, y in zip(range(1, num), range(num - 1, 0, -1)))
print(gen)
n = 1
while n < num:
    print(next(gen))
    n += 1
