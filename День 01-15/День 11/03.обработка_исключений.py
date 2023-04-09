"""
Python 3.9 Механизм исключения - состояние, которое может возникнуть при запущенном обработчике.
Название файла '03.обработка_исключений.py'

Version: 0.1
Author: Andrej Marinchenko
Date: 2023-04-09
"""

import time
import sys

filename = input('Пожалуйста, введите имя файла: ')
try:
    with open(filename) as f:
        lines = f.readlines()
except FileNotFoundError as msg:
    print('Невозможно открыть файл:', filename)
    print(msg)
except UnicodeDecodeError as msg:
    print('Нетекстовые файлы не могут быть декодированы')
    sys.exit()
else:
    for line in lines:
        print(line.rstrip())
        time.sleep(0.5)
finally:
    # Это лучшее место для реабилитации
    print('Я выполню все, что случится')
