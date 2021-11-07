"""
Python 3.9 Определите и используйте классы учащихся
Название файла '05.ученики.py'

Version: 0.1
Author: Andrej Marinchenko
Date: 2021-11-08
"""


def _foo():
    print('test')


class Student(object):

    # __init__ - это специальный метод, используемый для инициализации объекта при его создании
    # С помощью этого метода мы можем привязать два атрибута имени и возраста к объекту ученик
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def study(self, course_name):
        print('%sучится%s.' % (self.name, course_name))

    # PEP 8 требует, чтобы имя идентификатора было полностью в нижнем регистре, а несколько слов были соединены подчеркиванием
    # Но многие программисты и компании предпочитают использовать номенклатуру верблюжьих ящиков (логотип верблюжьих ящиков)
    def watch_av(self):
        if self.age < 18:
            print('%sможет смотреть только "Bears Haunted".' % self.name)
        else:
            print('смотрит фильм об островном государстве.' % self.name)


def main():
    stu1 = Student('Олег', 38)
    stu1.study('Программирование на Python')
    stu1.watch_av()
    stu2 = Student('Тимур', 15)
    stu2.study('Мысль и нравственность')
    stu2.watch_av()


if __name__ == '__main__':
    main()
