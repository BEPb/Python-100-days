"""
Python 3.10 Механизм исключения - состояние, которое может возникнуть при запущенном обработчике.
Название файла '02.обработка_исключений.py'

Version: 0.1
Author: Andrej Marinchenko
Date: 2023-04-09
"""

input_again = True
while input_again:
    try:
        a = int(input('a = '))
        b = int(input('b = '))
        print('%d / %d = %f' % (a, b, a / b))
        input_again = False
    except (ValueError, ZeroDivisionError) as msg:
        print(msg)
