"""
Python 3.9
Межпоточная связь (обмен данными) очень проста, потому что память одного и того же процесса может совместно использоваться
Межпроцессное взаимодействие (общие данные) проблематично, потому что операционная система будет защищать память, выделенную для процесса.
Чтобы добиться многопроцессорной связи, вы обычно можете использовать системные каналы, сокеты и трехсторонние службы.
multiprocessing.Queue
Поток демона
Демон-firewalld / httpd / mysqld
Процессы, которые не сохраняются, когда система не работает, не препятствуют остановке системы, потому что процесс еще не завершил выполнение.
Название файла 'example20.py'

Version: 0.1
Author: Andrej Marinchenko
Date: 2021-11-18
"""
from threading import Thread
from time import sleep


def output(content):
    while True:
        print(content, end='')


def main():
    Thread(target=output, args=('Ping', ), daemon=True).start()
    Thread(target=output, args=('Pong', ), daemon=True).start()
    sleep(5)
    print('bye!')


if __name__ == '__main__':
    main()
