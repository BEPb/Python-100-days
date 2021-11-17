"""
aiohttp-Асинхронный доступ к сети HTTP
Асинхронный ввод-вывод (асинхронное программирование) - только один поток (один поток) используется для обработки пользовательских запросов.
После того, как запрос пользователя принят, остальное - это операции ввода-вывода, а параллелизм также может быть достигнут за счет множественного мультиплексирования ввода-вывода.
Такой подход может повысить загрузку ЦП по сравнению с многопоточностью, поскольку отсутствуют накладные расходы на переключение потоков.
Redis / Node.js-однопоточный + асинхронный ввод-вывод
Сельдерей-асинхронная обработка трудоемких задач для выполнения
Цикл событий асинхронного ввода / вывода - uvloop
"""
import asyncio
import re

import aiohttp


async def fetch(session, url):
    async with session.get(url, ssl=False) as resp:
        return await resp.text()


async def main():
    pattern = re.compile(r'\<title\>(?P<title>.*)\<\/title\>')
    urls = ('https://www.python.org/',
            'https://git-scm.com/',
            'https://www.jd.com/',
            'https://www.taobao.com/',
            'https://www.douban.com/')
    async with aiohttp.ClientSession() as session:
        for url in urls:
            html = await fetch(session, url)
            print(pattern.search(html).group('title'))


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
    loop.close()
