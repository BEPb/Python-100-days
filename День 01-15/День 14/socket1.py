"""
ocket-Create сервер времени на основе протокола TCP

Version: 0.1
Author: 骆昊
Date: 2018-03-22
"""

from socket import *
from time import *

server = socket(AF_INET, SOCK_STREAM)
server.bind(('localhost', 6789))
server.listen()
print('Сервер запущен и ожидает подключения клиентов.')
while True:
    client, addr = server.accept()
    print('Клиент %s: %d успешно подключился.' % (addr[0], addr[1]))
    currtime = localtime(time())
    timestr = strftime('%Y-%m-%d %H:%M:%S', currtime)
    client.send(timestr.encode('utf-8'))
    client.close()
server.close()
