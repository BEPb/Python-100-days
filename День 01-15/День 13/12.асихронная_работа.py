"""
Python 3.9 Асинхронные операции ввода-вывода - async и await
Название файла '12.асихронная_работа.py'

Version: 0.1
Author: Andrej Marinchenko
Date: 2021-11-13
"""
import asyncio
import threading


# Функция, измененная async, больше не обычная функция, а сопрограмма
# Обратите внимание, что async и await будут отображаться как ключевые слова в Python 3.7
async def hello():
    print('%s: hello, world!' % threading.current_thread())
    await asyncio.sleep(2)
    print('%s: goodbye, world!' % threading.current_thread())


loop = asyncio.get_event_loop()
tasks = [hello(), hello()]
# Дождитесь завершения двух операций асинхронного ввода-вывода
loop.run_until_complete(asyncio.wait(tasks))
loop.close()
