"""
Python 3.10 При использовании многопоточности совершаем несколько задач загрузки
Название файла '03.многопоточная_загрузка.py'

Version: 0.1
Author: Andrej Marinchenko
Date: 2023-04-10
"""


from threading import Thread  # подключаем модуль многопоточной работы
from random import randint  # подключаем функцию генерации целых чисел
from time import time, sleep  # подключаем модуль работы со временем


def download_task(filename):  # функция-имитация загрузки файла (на входе имя файла)
    print('Начать загрузку %s...' % filename)  # перед загрузкой выводим сообщение на экран
    time_to_download = randint(5, 10)  # генерация случайного числа от 5 до 10
    sleep(time_to_download)  # ждем это случайное время
    print('Загрузка завершена! Потребовалось %d секунд' % time_to_download)  # выводим сообщение с отображением времени


def main():  # главная функция
    start = time()  # время начала выполнения программы
    thread1 = Thread(target=download_task, args=('Django.pdf',))  # создаем поток
    thread1.start()  # начало выполнения потока
    thread2 = Thread(target=download_task, args=('PyTorch.epub',))  # создаем поток
    thread2.start()  # начало выполнения потока
    thread1.join()  # ожидание выполнения
    thread2.join()  # ожидание выполнения
    end = time()  # время конца выполнения программы
    print('Всего потребовалось %.3f секунд..' % (end - start))  # сообщение о окончании с вычислением общего времени
    # загрузки


if __name__ == '__main__':  # если запущена это программа как главная
    main()  # запускаем главную функцию
