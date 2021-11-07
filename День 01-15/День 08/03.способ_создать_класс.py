"""
Python 3.9 Другой способ создать класс
Название файла '03.способ_создать_класс.py'

Version: 0.1
Author: Andrej Marinchenko
Date: 2021-11-08
"""


def bar(self, name):
    self._name = name


def foo(self, course_name):
    print('%s изучает %s.' % (self._name, course_name))


def main():
    Student = type('Student', (object,), dict(__init__=bar, study=foo))
    stu1 = Student('Олег')
    stu1.study('Программирование на Python')


if __name__ == '__main__':
    main()  
