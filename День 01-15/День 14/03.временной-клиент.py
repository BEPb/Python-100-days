"""
Python 3.9 временной-клиент
Название файла '03.временной-клиент.py'

Version: 0.1
Author: Andrej Marinchenko
Date: 2021-11-13
"""
from socket import socket


def main():
    client = socket()
    client.connect(('192.168.1.9', 6789))
    print(client.recv(1024).decode('utf-8'))
    client.close()


if __name__ == '__main__':  # если запущена это программа как главная
    main()  # запускаем главную функцию
