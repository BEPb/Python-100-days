"""
Python 3.10 файловый-клиент
Название файла '05.файловый-клиент.py'

Version: 0.1
Author: Andrej Marinchenko
Date: 2023-04-16
"""
from socket import socket
from json import loads
from base64 import b64decode


def main():  # главная функция
    client = socket()
    client.connect(('192.168.0.102', 5566))
    # Определить объект, который сохраняет двоичные данные
    in_data = bytes()
    # Поскольку я не знаю, насколько велики данные, отправляемые сервером, я получаю 1024 байта каждый раз
    data = client.recv(1024)
    while data:
        # Объединить полученные данные
        in_data += data
        data = client.recv(1024)
        # Декодировать полученные двоичные данные в строку JSON и преобразовать в словарь
        # Функция  # load - преобразовать строки JSON в объекты словаря.
    my_dict = loads(in_data.decode('utf-8'))
    filename = my_dict['filename']
    filedata = my_dict['filedata'].encode('utf-8')
    with open('/Users/admin/' + filename, 'wb') as f:
        # Декодировать данные формата base64 в двоичные данные и записывать их в файл
        f.write(b64decode(filedata))
    print('Картинка сохранена.')


if __name__ == '__main__':  # если запущена это программа как главная
    main()  # запускаем главную функцию
