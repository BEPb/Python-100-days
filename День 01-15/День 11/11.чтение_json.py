"""
Python 3.10 Чтение данных JSON
Название файла '11.чтение_json.py'

Version: 0.1
Author: Andrej Marinchenko
Date: 2023-04-09
"""

import json
# import csv2

json_str = '{"name": "Иван", "age": 35, "title": "математика"}'
result = json.loads(json_str)
print(result)
print(type(result))
print(result['name'])
print(result['age'])




