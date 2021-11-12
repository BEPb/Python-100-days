"""
Используйте центр экспресс-доставки coroutine-simulate для экспресс-доставки

Version: 0.1
Author: 骆昊
Date: 2018-03-21
"""

from time import sleep
from random import random


def build_deliver_man(man_id):
    total = 0
    while True:
        total += 1
        print('%d курьер готов забрать сегодняшний заказ %d.' % (man_id, total))
        pkg = yield
        print('Курьер с номером %d получил посылку с номером %s.' % (man_id, pkg))
        sleep(random() * 3)


def package_center(deliver_man, max_per_day):
    num = 1
    deliver_man.send(None)
    # next(deliver_man)
    while num <= max_per_day:
        package_id = 'PKG-%d' % num
        deliver_man.send(package_id)
        num += 1
        sleep(0.1)
    deliver_man.close()
    print('Сегодняшняя посылка доставлена!')


dm = build_deliver_man(1)
package_center(dm, 10)

# Хотя две функции не имеют отношения между вызовами, функция, которая создает курьера в качестве сопрограммы, помогает функции центра курьера выполнить задачу
# Подумайте, что делать, если курьеров несколько
