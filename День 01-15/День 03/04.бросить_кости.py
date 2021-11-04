"""
Бросьте кости, чтобы решить, что делать.
Название файла '04.бросить_кости.py'

Version: 0.1
Author: Andrej Marinchenko
Date: 2021-11-04
"""

from random import randint  # подключаем модуль рандомного (произвольного) значения

print("Пусть судьба подскажет, что нужно сделать")
face = randint(1, 6)
if face == 1:
    result = 'Поцеловать любимого человека'
elif face == 2:
    result = 'Бороться за свое мнение'
elif face == 3:
    result = 'Найти компромисс'
elif face == 4:
    result = 'Пойти спать'
elif face == 5:
    result = 'Пойти на дискотеку'
else:
    result = 'Ничего не делать'
print(result)
