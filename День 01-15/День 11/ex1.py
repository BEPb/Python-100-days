"""
Python 3.9 Механизм исключения - состояние, которое может возникнуть при запущенном обработчике.
Название файла '01.Связь_между_объектами.py'

Version: 0.1
Author: Andrej Marinchenko
Date: 2021-11-11
"""

input_again = True
while input_again:
    try:
        a = int(input('a = '))
        b = int(input('b = '))
        print('%d / %d = %f' % (a, b, a / b))
        input_again = False
    except ValueError:
        print('Пожалуйста, введите целое число')
    except ZeroDivisionError:
        print('Делитель не может быть 0')
# Обработка исключений, чтобы код не падал из-за исключений - это один из аспектов
# Что еще более важно, код может восстановиться после исключения, обработав исключение
