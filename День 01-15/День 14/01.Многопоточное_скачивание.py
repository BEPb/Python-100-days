"""
Python 3.9 Многопоточное скачивание
Название файла '01.Многопоточное_скачивание.py'

Version: 0.1
Author: Andrej Marinchenko
Date: 2021-11-13
"""

from threading import Thread
import requests


class DownloadHanlder(Thread):

    def __init__(self, url):
        super().__init__()
        self.url = url

    def run(self):
        filename = self.url[self.url.rfind('/') + 1:]
        resp = requests.get(self.url)
        with open('/Users/Downloads/' + filename, 'wb') as f:
            f.write(resp.content)


def main():  # главная функция
    # Получение сетевых ресурсов через функцию get модуля запросов
    resp = requests.get(
        'http://api.tianapi.com/meinv/?key=772a81a51ae5c780251b1f98ea431b84&num=10')
    # Разобрать данные в формате JSON, возвращенные сервером, в словарь
    data_model = resp.json()
    for mm_dict in data_model['newslist']:
        url = mm_dict['picUrl']
        # Реализуйте загрузку изображений через многопоточность
        DownloadHanlder(url).start()


if __name__ == '__main__':  # если запущена это программа как главная
    main()  # запускаем главную функцию
