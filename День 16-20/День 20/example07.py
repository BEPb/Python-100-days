"""
Python 3.10
программа осуществляет асинхронный обход нескольких web-страниц, извлечение их заголовков и вывод их на экран.
Название файла 'example07.py'

Version: 0.1
Author: Andrej Marinchenko
Date: 2023-05-13
"""

import asyncio  # Модуль asyncio используется для организации асинхронных операций
import re  # модуль re - для использования регулярных выражений
import aiohttp  # модуль aiohttp - для отправки HTTP-запросов и получения ответов на них


async def fetch(session, url):
    '''
    функция fetch(session, url) используется для отправки запросов и возврата ответа в виде строки
    '''
    async with session.get(url, ssl=False) as resp:
        return await resp.text()


async def main():
    '''
    Основная функция main(), в которой создается объект клиентской сессии aiohttp.ClientSession() для
    использования в методе fetch().

    В цикле for происходит обращение к нескольким url-адресам, получение ответов, извлечение из них заголовков с помощью
    регулярного выражения и вывод на экран с помощью метода print().

    '''
    pattern = re.compile(r'\<title\>(?P<title>.*)\<\/title\>')
    urls = ('https://www.python.org/',
            'https://git-scm.com/',
            'https://www.ibm.com/',
            'https://www.apple.com/',
            'https://www.google.com/')
    async with aiohttp.ClientSession() as session:
        for url in urls:
            html = await fetch(session, url)
            print(pattern.search(html).group('title'))


if __name__ == '__main__':
    '''    
    После запуска главной функции main(), используя module функцию asyncio.get_event_loop(), создается экземпляр 
    асинхронного цикла event loop и запускается функция main() с использованием метода loop.run_until_complete(main()).  
    
    Цикл запускает асинхронную функцию и ожидает ее завершения, после чего закрывается с помощью метода loop.close(). 
    '''
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
    # loop.close()
