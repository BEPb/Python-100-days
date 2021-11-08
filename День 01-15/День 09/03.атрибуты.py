"""
Python 3.9 Использование атрибутов
-Используйте существующие методы для определения аксессоров / модификаторов / удалителей
Название файла '03.атрибуты.py'

Version: 0.1
Author: Andrej Marinchenko
Date: 2021-11-09
"""


class Car(object):

    def __init__(self, brand, max_speed):
        self.set_brand(brand)
        self.set_max_speed(max_speed)

    def get_brand(self):
        return self._brand

    def set_brand(self, brand):
        self._brand = brand

    def get_max_speed(self):
        return self._max_speed

    def set_max_speed(self, max_speed):
        if max_speed < 0:
            raise ValueError('Invalid max speed for car')
        self._max_speed = max_speed

    def __str__(self):
        return 'Car: [Brand=%s, max speed=%d]' % (self._brand, self._max_speed)

    # Используйте существующие модификаторы и аксессоры для определения атрибутов
    brand = property(get_brand, set_brand)
    max_speed = property(get_max_speed, set_max_speed)


car = Car('QQ', 120)
print(car)
# ValueError
# car.max_speed = -100
car.max_speed = 320
car.brand = "Benz"
print(car)
print(Car.brand)
print(Car.brand.fget)
print(Car.brand.fset)
