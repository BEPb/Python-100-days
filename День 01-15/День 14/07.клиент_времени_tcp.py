"""
Python 3.9 Socket-Create Time Client на основе протокола TCP
Название файла '07.клиент_времени_tcp.py'

Version: 0.1
Author: Andrej Marinchenko
Date: 2021-11-13
"""

from socket import *

client = socket(AF_INET, SOCK_STREAM)
client.connect(('localhost', 6789))
while True:
    data = client.recv(1024)
    if not data:
        break
    print(data.decode('utf-8'))
client.close()
