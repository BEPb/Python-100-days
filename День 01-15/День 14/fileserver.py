from socket import socket, SOCK_STREAM, AF_INET
from base64 import b64encode
from json import dumps
from threading import Thread


def main():

    # Пользовательский класс потока
    class FileTransferHandler(Thread):

        def __init__(self, cclient):
            super().__init__()
            self.cclient = cclient

        def run(self):
            my_dict = {}
            my_dict['filename'] = 'guido.jpg'
            # JSON - это простой текст и не может переносить двоичные данные
            # Таким образом, двоичные данные изображения должны быть обработаны в кодировке base64
            my_dict['filedata'] = data
            # Преобразование словаря в строку JSON с помощью функции дампа
            json_str = dumps(my_dict)
            # Отправить строку JSON
            self.cclient.send(json_str.encode('utf-8'))
            self.cclient.close()

    # 1. Создайте объект сокета и укажите, какой транспортный сервис использовать.
    server = socket()
    # 2. Привязать IP-адрес и порт (чтобы различать разные сервисы)
    server.bind(('192.168.1.2', 5566))
    # 3. Включите мониторинг-прослушивание клиентских подключений к серверу.
    server.listen(512)
    print('Сервер запускается и начинает слушать .....')
    with open('guido.jpg', 'rb') as f:
        # Обработать двоичные данные в base64 и затем декодировать их в строку
        data = b64encode(f.read()).decode('utf-8')
    while True:
        client, addr = server.accept()
        # Используйте словарь (пара ключ-значение) для сохранения различных данных для отправки
        # Позже словарь может быть преобразован в формат JSON и передан по сети
        FileTransferHandler(client).start()


if __name__ == '__main__':
    main()
