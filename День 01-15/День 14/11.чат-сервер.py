"""
Python 3.9 Socket чат-сервер
Название файла '11.чат-сервер.py'

Version: 0.1
Author: Andrej Marinchenko
Date: 2021-11-13
"""
from socket import socket
from threading import Thread


def main():  # главная функция

    class ClientHandler(Thread):

        def __init__(self, client):
            super().__init__()
            self._client = client

        def run(self):
            try:
                while True:
                    try:
                        data = self._client.recv(1024)
                        if data.decode('utf-8') == 'byebye':
                            clients.remove(self._client)
                            self._client.close()
                            break
                        else:
                            for client in clients:
                                client.send(data)
                    except Exception as e:
                        print(e)
                        clients.remove(self._client)
                        break
            except Exception as e:
                print(e)

    server = socket()
    server.bind(('10.7.189.118', 12345))
    server.listen(512)
    clients = []
    while True:
        curr_client, addr = server.accept()
        print(addr[0], 'Подключиться к серверу.')
        clients.append(curr_client)
        ClientHandler(curr_client).start()


if __name__ == '__main__':  # если запущена это программа как главная
    main()  # запускаем главную функцию
