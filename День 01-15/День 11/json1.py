"""
Python 3.9 Чтение данных JSON
Название файла '01.Связь_между_объектами.py'

Version: 0.1
Author: Andrej Marinchenko
Date: 2021-11-11
"""

import json
import csv2

json_str = '{"name": "Иван", "age": 35, "title": "математика"}'
result = json.loads(json_str)
print(result)
print(type(result))
print(result['name'])
print(result['age'])

# Передать преобразованный словарь как параметр ключевого слова конструктору Учителя
teacher = csv2.Teacher(**result)
print(teacher)
print(teacher.name)
print(teacher.age)
print(teacher.title)


