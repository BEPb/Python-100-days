"""
Используйте класс Process для создания нескольких процессов

Version: 0.1
Author: 骆昊
Date: 2018-03-20
"""

# Результат выполнения следующей программы может подтвердить, что родительский процесс скопировал процесс и его структуру данных при создании дочернего процесса
# Каждый процесс имеет собственное независимое пространство памяти, поэтому обмен данными между процессами может осуществляться только через IPC



from multiprocessing import Process, Queue, current_process
from time import sleep


def sub_task(content, counts):
    print(f'PID: {current_process().pid}')
    counter = 0
    while counter < counts:
        counter += 1
        print(f'{counter}: {content}')
        sleep(0.01)


def main():
    number = random.randrange(5, 10)
    Process(target=sub_task, args=('Ping', number)).start()
    Process(target=sub_task, args=('Pong', number)).start()


if __name__ == '__main__':
    main()
