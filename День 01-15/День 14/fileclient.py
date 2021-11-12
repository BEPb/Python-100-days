from socket import socket
from json import loads
from base64 import b64decode


def main():
    client = socket()
    client.connect(('192.168.1.2', 5566))
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
    with open('/Users/Hao/' + filename, 'wb') as f:
        # Декодировать данные формата base64 в двоичные данные и записывать их в файл
        f.write(b64decode(filedata))
    print('Картинка сохранена.')


if __name__ == '__main__':
    main()
