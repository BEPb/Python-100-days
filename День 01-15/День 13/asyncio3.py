"""
Модуль асинхронной операции ввода-вывода asyncio

Version: 0.1
Author: 骆昊
Date: 2018-03-21
"""
import asyncio


async def wget(host):
    print('wget %s...' % host)
    connect = asyncio.open_connection(host, 80)
    # Асинхронно ждать результата подключения
    reader, writer = await connect
    header = 'GET / HTTP/1.0\r\nHost: %s\r\n\r\n' % host
    writer.write(header.encode('utf-8'))
    # Выполнить операцию записи в режиме асинхронного ввода-вывода
    await writer.drain()
    while True:
        # Выполнять операции чтения в режиме асинхронного ввода-вывода
        line = await reader.readline()
        if line == b'\r\n':
            break
        print('%s header > %s' % (host, line.decode('utf-8').rstrip()))
    writer.close()


loop = asyncio.get_event_loop()
# Создайте список из трех сопрограмм с помощью генеративной грамматики
hosts_list = ['www.sina.com.cn', 'www.sohu.com', 'www.163.com']
tasks = [wget(host) for host in hosts_list]
# Следующий метод помещает операции асинхронного ввода-вывода в EventLoop до завершения выполнения
loop.run_until_complete(asyncio.wait(tasks))
loop.close()
