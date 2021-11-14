"""
Python 3.9 Вычисление последовательно в 8 процессов.
Название файла '10.многопроцессорная_работа.py'

Version: 0.1
Author: Andrej Marinchenko
Date: 2021-11-13
"""

from multiprocessing import Process, Queue
from time import time


def task_handler(curr_list, result_queue):
    total = 0
    for number in curr_list:
        total += number
    result_queue.put(total)


def main():  # главная функция
    processes = []
    number_list = [x for x in range(1, 100000001)]
    result_queue = Queue()
    index = 0
    # разбиваем задачу на 8 процессов
    for _ in range(8):
        p = Process(target=task_handler,
                    args=(number_list[index:index + 12500000], result_queue))
        index += 12500000
        processes.append(p)
        p.start()
    start = time()  # время начала выполнения программы
    for p in processes:
        p.join()  # ожидаем окончание каждого процесса

    total = 0
    while not result_queue.empty():
        total += result_queue.get()
    print(total)
    end = time()
    print('Execution time: ', (end - start), 's', sep='')


if __name__ == '__main__':  # проверка основной программы
    main()  # запуск главной функции