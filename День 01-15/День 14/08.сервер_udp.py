"""
Python 3.9 Сервер Socket-Echo на основе протокола UDP
Название файла '08.сервер_udp.py'

Version: 0.1
Author: Andrej Marinchenko
Date: 2021-11-13
"""
from socket import *


server = socket(AF_INET, SOCK_DGRAM)
server.bind(('localhost', 6789))
while True:
    data, addr = server.recvfrom(1024)
    server.sendto(data, addr)
server.close()
