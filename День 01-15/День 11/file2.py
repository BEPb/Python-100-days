"""
Python 3.9 Прочтите файл pi, чтобы определить, содержит ли он ваш собственный день рождения
Название файла '01.Связь_между_объектами.py'

Version: 0.1
Author: Andrej Marinchenko
Date: 2021-11-11
"""

birth = input('Укажите свой день рождения: ')
with open('97.pi_million_digits.txt') as f:
    lines = f.readlines()
    pi_string = ''
    for line in lines:
        pi_string += line.strip()
    if birth in pi_string:
        print('Bingo!!!')
