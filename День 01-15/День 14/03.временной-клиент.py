"""
Python 3.10 временной-клиент
Название файла '03.временной-клиент.py'

Version: 0.1
Author: Andrej Marinchenko
Date: 2023-04-15
"""
from socket import socket


def main():
    client = socket()
    client.connect(('192.168.1.9', 12345))  # указываем IP адрес и порт временного сервера
    print(client.recv(1024).decode('utf-8'))
    client.close()


if __name__ == '__main__':  # если запущена это программа как главная
    main()  # запускаем главную функцию
