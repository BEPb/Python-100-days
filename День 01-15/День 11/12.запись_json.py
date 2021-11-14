"""
Python 3.9 Записать в файл JSON
Название файла '12.запись_json.py'

Version: 0.1
Author: Andrej Marinchenko
Date: 2021-11-11
"""

import json

teacher_dict = {'name': 'Иван', 'age': 25, 'title': 'химия'}
json_str = json.dumps(teacher_dict)
print(json_str)
print(type(json_str))
fruits_list = ['apple', 'orange', 'strawberry', 'banana', 'pitaya']
json_str = json.dumps(fruits_list)
print(json_str)
print(type(json_str))
