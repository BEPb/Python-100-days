"""
Python 3.9 Зависимости между объектами и перегрузкой оператора
Название файла '04.зависимости.py'

Version: 0.1
Author: Andrej Marinchenko
Date: 2021-11-09
"""


class Car(object):

    def __init__(self, brand, max_speed):
        self._brand = brand
        self._max_speed = max_speed
        self._current_speed = 0

    @property
    def brand(self):
        return self._brand

    def accelerate(self, delta):
        self._current_speed += delta
        if self._current_speed > self._max_speed:
            self._current_speed = self._max_speed

    def brake(self):
        self._current_speed = 0

    def __str__(self):
        return '%sтекущую скорость%d' % (self._brand, self._current_speed)


class Student(object):

    def __init__(self, name, age):
        self._name = name
        self._age = age

    @property
    def name(self):
        return self._name

    # Между учеником и машиной существует зависимость - ученик пользуется машиной
    def drive(self, car):
        print('%sсчастливо водил%sпо дороге на запад' % (self._name, car._brand))
        car.accelerate(30)
        print(car)
        car.accelerate(50)
        print(car)
        car.accelerate(50)
        print(car)

    def study(self, course_name):
        print('%sизучает%s.' % (self._name, course_name))

    def watch_av(self):
        if self._age >= 18:
            print('%sсмотрит фильмы без ограничений.' % self._name)
        else:
            print('%sсмотрит фильмы с ограничениями.' % self._name)

    # Перегрузить оператор больше (>)
    def __gt__(self, other):
        return self._age > other._age

    # Перегружаем оператор меньше (<)
    def __lt__(self, other):
        return self._age < other._age


if __name__ == '__main__':
    stu1 = Student('Иван', 38)
    stu1.study('Программирование на Python')
    stu1.watch_av()
    stu2 = Student('Костя', 15)
    stu2.study('Мысль и нравственность')
    stu2.watch_av()
    car = Car('QQ', 120)
    stu2.drive(car)
    print(stu1 > stu2)
    print(stu1 < stu2)
