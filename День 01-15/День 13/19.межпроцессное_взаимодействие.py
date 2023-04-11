"""
Python 3.10 Осуществляйте межпроцессное взаимодействие
Название файла '19.межпроцессное_взаимодействие.py'

Version: 0.1
Author: Andrej Marinchenko
Date: 2023-04-10
"""
import multiprocessing
import os


def sub_task(queue):
    print('Номер дочернего процесса:', os.getpid())
    counter = 0
    while counter < 1000:
        queue.put('Pong')
        counter += 1


if __name__ == '__main__':
    print('Текущий номер процесса:', os.getpid())
    queue = multiprocessing.Queue()
    p = multiprocessing.Process(target=sub_task, args=(queue,))
    p.start()
    counter = 0
    while counter < 1000:
        queue.put('Ping')
        counter += 1
    p.join()
    print('Подзадача выполнена.')
    for _ in range(2000):
        print(queue.get(), end='')
