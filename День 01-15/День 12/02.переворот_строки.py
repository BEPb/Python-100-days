"""
Python 3.9 Общие методы-операции со строками для переворота строк
Название файла '02.переворот_строки.py'

Version: 0.1
Author: Andrej Marinchenko
Date: 2021-11-11
"""

from io import StringIO


def reverse_str1(str):
    return str[::-1]


def reverse_str2(str):
    if len(str) <= 1:
        return str
    return reverse_str2(str[1:]) + str[0:1]


def reverse_str3(str):
    # Объекты StringIO - это переменные строки в Python
    # Вы не должны использовать неизменяемые строки для операций конкатенации строк, потому что будет сгенерировано много бесполезных строковых объектов
    rstr = StringIO()
    str_len = len(str)
    for index in range(str_len - 1, -1, -1):
        rstr.write(str[index])
    return rstr.getvalue()


def reverse_str4(str):
    return ''.join(str[index] for index in range(len(str) - 1, -1, -1))


def reverse_str5(str):
    # Преобразуем строку в список
    str_list = list(str)
    str_len = len(str)
    # Используйте функцию zip для объединения двух последовательностей в один итератор, который создает кортежи
    # Каждый раз вы можете получить два нижних индекса, один передний и один задний, чтобы добиться обмена элементами
    for i, j in zip(range(str_len // 2), range(str_len - 1, str_len // 2, -1)):
        str_list[i], str_list[j] = str_list[j], str_list[i]
    # Объединить элементы списка в строки
    return ''.join(str_list)


if __name__ == '__main__':
    str = 'I love Python'
    print(reverse_str1(str))
    print(str)
    print(reverse_str2(str))
    print(str)
    print(reverse_str3(str))
    print(str)
    print(reverse_str4(str))
    print(str)
    print(reverse_str5(str))
    print(str)
