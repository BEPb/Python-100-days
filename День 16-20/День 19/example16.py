"""
Python 3.9
Магический метод
Если вы хотите поместить настраиваемый объект в набор или использовать его в качестве ключа dict
Затем вы должны переписать два магических метода __hash__ и __eq__.
Первый используется для вычисления хэш-кода объекта, а второй используется для определения того, являются ли два объекта
 одинаковыми.
Объекты с разными хэш-кодами должны быть разными объектами, но один и тот же хэш-код не обязательно может быть одним и
тем же объектом (конфликт хеш-кода)
Поэтому, когда хэш-коды совпадают, __eq__ используется для определения того, являются ли объекты одинаковыми.
Название файла 'example16.py'

Version: 0.1
Author: Andrej Marinchenko
Date: 2021-11-18
"""


class Student():
    __slots__ = ('stuid', 'name', 'gender')

    def __init__(self, stuid, name):
        self.stuid = stuid
        self.name = name

    def __hash__(self):
        return hash(self.stuid) + hash(self.name)

    def __eq__(self, other):
        return self.stuid == other.stuid and \
            self.name == other.name

    def __str__(self):
        return f'{self.stuid}: {self.name}'

    def __repr__(self):
        return self.__str__()


class School():

    def __init__(self, name):
        self.name = name
        self.students = {}

    def __setitem__(self, key, student):
        self.students[key] = student

    def __getitem__(self, key):
        return self.students[key]


def main():
    # students = set()
    # students.add(Student(1001, 'Ванька'))
    # students.add(Student(1001, 'Петька'))
    # students.add(Student(1001, 'Сашка'))
    # print(len(students))
    # print(students)
    stu = Student(1234, 'Костян')
    stu.gender = 'Male'
    # stu.birth = '1980-11-28'
    print(stu.name, stu.birth)
    school = School('средняя школа №1')
    school[1001] = Student(1001, 'Женька')
    school[1002] = Student(1002, 'Колька')
    school[1003] = Student(1003, 'Русел')
    print(school[1002])
    print(school[1003])


if __name__ == '__main__':
    main()

