"""
Python 3.9
декораторы - декораторы, как правило, размещены в кросс-concern функции
	так называемая функция сквозного внимания является функцией, которая будет использоваться во многих местах, но не обязательно связана с нормальным бизнесом и логикой
	ДЕКОРАТОР НА САМОМ ДЕЛЕ РЕАЛИЗУЕТ ПРОКСИ-РЕЖИМ В РЕЖИМЕ ПРОЕКТИРОВАНИЯ - AOP (ПРОГРАММИРОВАНИЕ ДЛЯ СЕЧЕНИЯ)
Название файла 'example09.py'

Version: 0.1
Author: Andrej Marinchenko
Date: 2021-11-18
"""
from functools import wraps
from random import randint
from time import time, sleep

import pymysql


def record(output):

    def decorate(func):

        @wraps(func)
        def wrapper(*args, **kwargs):
            start = time()
            ret_value = func(*args, **kwargs)
            output(func.__name__, time() - start)
            return ret_value

        return wrapper

    return decorate


def output_to_console(fname, duration):
    print('%s: %.3f секунд' % (fname, duration))


def output_to_file(fname, duration):
    with open('log.txt', 'a') as file_stream:
        file_stream.write('%s: %.3f секунд\n' % (fname, duration))


def output_to_db(fname, duration):
    con = pymysql.connect(host='localhost', port=3306,
                          database='test', charset='utf8',
                          user='root', password='123456',
                          autocommit=True)
    try:
        with con.cursor() as cursor:
            cursor.execute('insert into tb_record values (default, %s, %s)',
                           (fname, '%.3f' % duration))
    finally:
        con.close()


@record(output_to_console)
def random_delay(min, max):
    sleep(randint(min, max))


def main():
    for _ in range(3):
        # print(random_delay.__name__)
        random_delay(3, 5)
    # for _ in range(3):
    #     # отмените декоратор
    #     random_delay.__wrapped__(3, 5)


if __name__ == '__main__':
    main()
