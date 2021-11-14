"""
Python 3.9 Socket чат-клиент
Название файла '12.чат-клиент.py'

Version: 0.1
Author: Andrej Marinchenko
Date: 2021-11-13
"""
from socket import socket
from threading import Thread


def main():  # главная функция

    class RefreshScreenThread(Thread):

        def __init__(self, client):
            super().__init__()
            self._client = client

        def run(self):
            while running:
                data = self._client.recv(1024)
                print(data.decode('utf-8'))

    nickname = input('Пожалуйста, введите свой ник: ')
    myclient = socket()
    myclient.connect(('10.7.189.118', 12345))
    running = True
    RefreshScreenThread(myclient).start()
    while running:
        content = input('Пожалуйста, говорите: ')
        if content == 'byebye':
            myclient.send(content.encode('utf-8'))
            running = False
        else:
            msg = nickname + ': ' + content
            myclient.send(msg.encode('utf-8'))


if __name__ == '__main__':  # если запущена это программа как главная
    main()  # запускаем главную функцию
