"""
Не используйте многопоточность - имитируйте несколько задач загрузки

Version: 0.1
Author: 骆昊
Date: 2018-03-20
"""

from random import randint
from time import time, sleep


def download_task(filename):
    print('Начать загрузку %s...' % filename)
    time_to_download = randint(5, 10)
    sleep(time_to_download)
    print('Загрузка завершена! Потребовалось %d секунд' % time_to_download)


def main():
    start = time()
    download_task('Python.pdf')
    download_task('Peking.avi')
    end = time()
    print('Всего заняло% .2f секунд.' % (end - start))


if __name__ == '__main__':
    main()
