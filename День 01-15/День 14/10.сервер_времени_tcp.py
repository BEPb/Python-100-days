"""
Python 3.9 Socket-Create сервер времени на основе протокола TCP
Название файла '10.сервер_времени_tcp.py'

Version: 0.1
Author: Andrej Marinchenko
Date: 2021-11-13
"""
from socketserver import TCPServer, StreamRequestHandler
from time import *


class EchoRequestHandler(StreamRequestHandler):

    def handle(self):  # главная функция
        currtime = localtime(time())
        timestr = strftime('%Y-%m-%d %H:%M:%S', currtime)
        self.wfile.write(timestr.encode('utf-8'))


server = TCPServer(('localhost', 6789), EchoRequestHandler)
server.serve_forever()
