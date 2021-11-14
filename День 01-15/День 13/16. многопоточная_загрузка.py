"""
Python 3.9 При использовании многопоточности совершите несколько задач загрузки
Название файла '16. многопоточная_загрузка.py'

Version: 0.1
Author: Andrej Marinchenko
Date: 2021-11-11
"""

from random import randint
from time import time, sleep
import atexit
import _thread


def download_task(filename):
    print('Начать загрузку %s...' % filename)
    time_to_download = randint(5, 10)
    print('Оставшееся время %d секунд.' % time_to_download)
    sleep(time_to_download)
    print('%s загрузка завершена!' % filename)


def shutdown_hook(start):
    end = time()
    print('Всего потребовалось %.3f секунд..' % (end - start))


def main():
    start = time()
    # Поместите несколько задач загрузки в несколько потоков для выполнения
    thread1 = _thread.start_new_thread(download_task, ('Python.pdf',))
    thread2 = _thread.start_new_thread(download_task, ('Hot.avi',))
    # Зарегистрируйте ловушку выключения для расчета времени выполнения до окончания выполнения программы
    atexit.register(shutdown_hook, start)


if __name__ == '__main__':  # если запущена это программа как главная
    main()  # запускаем главную функцию

