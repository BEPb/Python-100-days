"""
ри использовании многопоточности имитируйте несколько задач загрузки

Version: 0.1
Author: 骆昊
Date: 2018-03-20
"""

from random import randint
from time import time, sleep
import threading


class DownloadTask(threading.Thread):

    def __init__(self, filename):
        super().__init__()
        self._filename = filename

    def run(self):
        print('Начать загрузку %s...' % self._filename)
        time_to_download = randint(5, 10)
        print('Оставшееся время %d секунд.' % time_to_download)
        sleep(time_to_download)
        print('%s загрузка завершена!' % self._filename)


def main():
    start = time()
    # Поместите несколько задач загрузки в несколько потоков для выполнения
    # Создайте объект потока через собственный класс потока.После запуска потока он обратится к нему и выполнит метод run.
    thread1 = DownloadTask('Python.pdf')
    thread1.start()
    thread2 = DownloadTask('Peking.avi')
    thread2.start()
    thread1.join()
    thread2.join()
    end = time()
    print('Всего затрачено %.3f секунд' % (end - start))


if __name__ == '__main__':
    main()

# Обратите внимание, что потоки, созданные с помощью threading.Thread, по умолчанию не являются потоками демона
