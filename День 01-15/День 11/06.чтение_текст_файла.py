"""
Python 3.10 Прочтите файл pi, чтобы определить, содержит ли он ваш собственный день рождения
Название файла '06.чтение_текст_файла.py'

Version: 0.1
Author: Andrej Marinchenko
Date: 2023-04-09
"""

birth = input('Укажите свой день рождения: ')
with open('97.pi_million_digits.txt') as f:
    lines = f.readlines()
    pi_string = ''
    for line in lines:
        pi_string += line.strip()
    if birth in pi_string:
        print('Bingo!!!')
