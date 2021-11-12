"""
Использование сопрограммы - просмотр статуса сопрограммы

Version: 0.1
Author: 骆昊
Date: 2018-03-21
"""

from time import sleep
from inspect import getgeneratorstate


def build_deliver_man(man_id):
    total = 0
    while True:
        total += 1
        print('%d курьер готов забрать сегодняшний заказ %d.' % (man_id, total))
        pkg = yield
        print('Курьер с номером %d получил посылку с номером %s.' % (man_id, pkg))
        sleep(0.5)


def package_center(deliver_man, max_per_day):
    num = 1
    # Создано состояние (GEN_CREATED) - ожидание начала выполнения
    print(getgeneratorstate(deliver_man))
    deliver_man.send(None)
    # Приостановленное состояние (GEN_SUSPENDED) - пауза в выражении yield
    print(getgeneratorstate(deliver_man))
    # следующий (delivery_man)
    while num <= max_per_day:
        package_id = 'PKG-%d' % num
        deliver_man.send(package_id)
        num += 1
    deliver_man.close()
    # Конечное состояние (GEN_CLOSED) - выполнение завершено
    print(getgeneratorstate(deliver_man))
    print('今天的包裹派送完毕!')


dm = build_deliver_man(1)
package_center(dm, 10)
