"""
Python 3.9 Socket-Create Echo клиент на основе протокола UDP
Название файла '09.клиент_udp.py'

Version: 0.1
Author: Andrej Marinchenko
Date: 2021-11-13
"""

from socket import *

client = socket(AF_INET, SOCK_DGRAM)
while True:
    data_str = input('Пожалуйста, введите: ')
    client.sendto(data_str.encode('utf-8'), ('localhost', 6789))
    data, addr = client.recvfrom(1024)
    data_str = data.decode('utf-8')
    print('Ответ сервера:', data_str)
    if data_str == 'bye':
        break
client.close()
