"""
Модуль асинхронной операции ввода-вывода asyncio

Version: 0.1
Author: 骆昊
Date: 2018-03-21
"""

import asyncio
import threading
# import time


@asyncio.coroutine
def hello():
    print('%s: hello, world!' % threading.current_thread())
    # Сон не блокирует основной поток из-за использования асинхронных операций ввода-вывода
    # Обратите внимание, что есть выход из ожидания завершения операции сна
    yield from asyncio.sleep(2)
    # asyncio.sleep(1)
    # time.sleep(1)
    print('%s: goodbye, world!' % threading.current_thread())


loop = asyncio.get_event_loop()
tasks = [hello(), hello()]
# Дождитесь завершения двух операций асинхронного ввода-вывода
loop.run_until_complete(asyncio.wait(tasks))
print('game over!')
loop.close()
