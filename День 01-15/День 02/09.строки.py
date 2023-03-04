"""
Общие операции со строками
Название файла '09.строки.py'

Version: 0.1
Author: Andrej Marinchenko
Date: 2023-03-04
"""

str1 = 'привет, мир!'

print('Первая буква каждого слова заглавная: ', str1.title())
print('Строка заглавными буквами: ', str1.upper())
print('Длина строки:', len(str1))
print('Строка в верхнем регистре: ', str1.isupper())  # False
print('Начинается ли строка с привет: ', str1.startswith('привет'))
print('Есть ли в конце строки с привет: ', str1.endswith('привет'))  # False
print('Начинается ли строка с восклицательного знака: ', str1.startswith('!'))  # False
print('Заканчивается ли строка восклицательным знаком: ', str1.endswith('!'))  # True
str3 = str1.title() + ' ' + str1.upper()  # соединяем строки в новую переменную str3
print(str3)
