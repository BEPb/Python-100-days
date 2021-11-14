"""
Python 3.9 временной-сервер
Название файла '02.временной-сервер.py'

Version: 0.1
Author: Andrej Marinchenko
Date: 2021-11-13
"""

from socket import socket, SOCK_STREAM, AF_INET
from datetime import datetime


def main():
    # 1. Создайте объект сокета и укажите, какой транспортный сервис использовать.
    # family=AF_INET - IPv4 адрес
    # family=AF_INET6 - IPv6 адрес
    # type=SOCK_STREAM - TCP сокет
    # type=SOCK_DGRAM - UDP сокет
    # type=SOCK_RAW - raw сокет
    server = socket(family=AF_INET, type=SOCK_STREAM)
    # 2.Привязать IP-адрес и порт (чтобы различать разные сервисы)
    server.bind(('192.168.1.2', 6789))
    # 3.Включите мониторинг-прослушивание клиентских подключений к серверу.
    server.listen(512)
    print('Сервер запускается и начинает слушать...')
    # 4.Получение соединения клиента по шлейфу и выполнение соответствующей обработки (предоставление услуг)
    while True:
        # Метод accept - это метод блокировки, если к серверу не подключен клиент
        # Этот метод заблокирует код и не будет выполняться вниз
        # метод accept возвращает первый элемент кортежа - это клиентский объект
        # Второй элемент - это адрес клиента (состоит из двух частей: IP и порт)
        client, addr = server.accept()
        print(str(addr) + 'Подключено к серверу.')
        # 5.Отправить данные
        client.send(str(datetime.now()).encode('utf-8'))
        # 6.Отключитесь
        client.close()


if __name__ == '__main__':  # если запущена это программа как главная
    main()  # запускаем главную функцию
