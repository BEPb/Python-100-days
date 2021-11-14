"""
Python 3.9 Записать в файл CSV
Название файла '10.запись_csv.py'

Version: 0.1
Author: Andrej Marinchenko
Date: 2021-11-11
"""

import csv


class Teacher(object):

    def __init__(self, name, age, title):
        self.__name = name
        self.__age = age
        self.__title = title
        self.__index = -1

    @property
    def name(self):
        return self.__name

    @property
    def age(self):
        return self.__age

    @property
    def title(self):
        return self.__title


filename = '98.teacher.csv'
teachers = [Teacher('Антон', 38, 'математика'), Teacher('Юля', 25, 'физика')]

try:
    with open(filename, 'w') as f:
        writer = csv.writer(f)
        for teacher in teachers:
            writer.writerow([teacher.name, teacher.age, teacher.title])
except BaseException as e:
    print('Невозможно записать файл:', filename)
else:
    print('Сохранение данных завершено!')
