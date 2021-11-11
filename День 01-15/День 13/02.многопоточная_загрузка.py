"""
Python 3.9 При использовании многопоточности совершите несколько задач загрузки
Название файла '02.многопоточная_загрузка.py'

Version: 0.1
Author: Andrej Marinchenko
Date: 2021-11-11
"""

from random import randint
from threading import Thread
from time import time, sleep


def download_task(filename):
    print('Начать загрузку %s...' % filename)
    time_to_download = randint(5, 10)
    sleep(time_to_download)
    print('%s загрузка завершена! Потребовалось %d секунд' % (filename, time_to_download))


def main():
    start = time()
    thread1 = Thread(target=download_task, args=('Python.pdf',))
    thread1.start()
    thread2 = Thread(target=download_task, args=('Hot.avi',))
    thread2.start()
    thread1.join()
    thread2.join()
    end = time()
    print('Всего потребовалось %.3f секунд..' % (end - start))


if __name__ == '__main__':
    main()
