"""
Python 3.9 Использование атрибутов
-Аксессор / модификатор / удалитель
-Используйте __slots__ для ограничения атрибутов
Название файла '02.атрибуты.py'

Version: 0.1
Author: Andrej Marinchenko
Date: 2021-11-09
"""


class Car(object):

    __slots__ = ('_brand', '_max_speed')

    def __init__(self, brand, max_speed):
        self._brand = brand
        self._max_speed = max_speed

    @property
    def brand(self):
        return self._brand

    @brand.setter
    def brand(self, brand):
        self._brand = brand

    @brand.deleter
    def brand(self):
        del self._brand

    @property
    def max_speed(self):
        return self._max_speed

    @max_speed.setter
    def max_speed(self, max_speed):
        if max_speed < 0:
            raise ValueError('Invalid max speed for car')
        self._max_speed = max_speed

    def __str__(self):
        return 'Car: [Brand=%s, max speed=%d]' % (self._brand, self._max_speed)


car = Car('QQ', 120)
print(car)
# ValueError
# car.max_speed = -100
car.max_speed = 320
car.brand = "Benz"
# Следующий код вызовет исключение после использования ограничения атрибута __slots__
# car.current_speed = 80
print(car)
# Если предоставляется средство удаления, следующий код может быть выполнен
# del car.brand
# Реализация атрибутов
print(Car.brand)
print(Car.brand.fget)
print(Car.brand.fset)
print(Car.brand.fdel)
# Используйте приведенный выше код, чтобы помочь учащимся понять концепцию оболочки, упомянутую ранее
# В Python много похожего синтаксического сахара, и подобные вещи появятся позже
