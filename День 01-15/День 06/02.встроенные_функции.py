"""
Python 3.10 Встроенные функции Python
-Математика: abs / divmod / pow / round / min / max / sum
-Последовательность корреляции: len / range / next / filter / map / sorted / slice / reverse
-Преобразование типов: chr / ord / str / bool / int / float / complex / bin / oct / hex
-Структура данных: dict / list / set / tuple
-Другие функции: all / any / id / input / open / print / type
Название файла '02.встроенные_функции.py'

Version: 0.1
Author: Andrej Marinchenko
Date: 2023-03-04
"""


def myfilter(mystr):  # функция фильтрации
    return len(mystr) == 6  # если длинни слова равна 6 символам

print(abs(-1.2345))  # функция получения абсолютного значения
print(round(-1.2345))  # функция округления числа
print(pow(1.2345, 5))  # функция возвращает результат возведения числа в степень, с опциональным делением по модулю
fruits = ['апельсин', 'персик', 'дуриан', 'арбуз']  # создаем список фруктов
print(fruits[slice(1, 3)])  # печатаем 1 и 2 фрукт в списке (не печатаем нулевой и третий)
fruits2 = list(filter(myfilter, fruits))  # фильтруем список, оставляя только фрукты из 6 букв
print(fruits)  # печатаем первый список
print(fruits2)  # печатаем второй, отфильтрованный список
