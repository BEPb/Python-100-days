"""
Python 3.9 Общие операции со строками
Название файла '01.операции_строки.py'

Version: 0.1
Author: Andrej Marinchenko
Date: 2021-11-11
"""

import pyperclip

# Escape character
print('My brother\'s name is \'007\'')
# Исходная строка
print(r'My brother\'s name is \'007\'')

str = 'hello123world'
print('he' in str)
print('her' in str)
# Строка содержит только буквы
print(str.isalpha())
# Строка содержит только буквы и цифры
print(str.isalnum())
# Строка содержит только числа
print(str.isdecimal())

print(str[0:5].isalpha())
print(str[5:8].isdecimal())

list = ['Лунный свет перед кроватью', 'Подозреваемый иней на земле', 'Посмотри на луну', 'Склони голову и подумай о родном городе']
print('-'.join(list))
sentence = 'You go your way I will go mine'
words_list = sentence.split()
print(words_list)
email = 'jackfrued@126.com'
print(email)
print(email.strip())
print(email.lstrip())

# Поместите текст в системный буфер обмена
pyperclip.copy('Если тигр не пришлет кошку, ты относишься ко мне как к умирающему')
# Получить текст из системного буфера обмена
# print(pyperclip.paste())
