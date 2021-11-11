"""
Python 3.9 Прочитать файл CSV
Название файла '01.Связь_между_объектами.py'

Version: 0.1
Author: Andrej Marinchenko
Date: 2021-11-10
"""

import csv

filename = 'example.csv'

try:
    with open(filename) as f:
        reader = csv.reader(f)
        data = list(reader)
except FileNotFoundError:
    print('Невозможно открыть файл:', filename)
else:
    for item in data:
        print('%-30s%-20s%-10s' % (item[0], item[1], item[2]))
