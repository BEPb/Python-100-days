"""
Python 3.10 Многопоточное скачивание
Название файла '01.Многопоточное_скачивание.py'

Version: 0.1
Author: Andrej Marinchenko
Date: 2023-04-15
"""
import requests
import threading

# Список URL для скачивания
urls = ['https://i.postimg.cc/yNdnFR8y/Screenshot-11.png', 'https://i.postimg.cc/BvmWNyF3/Screenshot-3.png', 'https://i.postimg.cc/g2WN0XZb/Screenshot-1.png']


def download(url):
    # Отправить запрос GET и сохранить содержимое ответа в файл
    response = requests.get(url)
    with open(url.split('/')[-1], 'wb') as file:
        file.write(response.content)
    print(f'Скачивание по ссылке {url} заврешено')


if __name__ == '__main__':
    # Создайте новый поток для каждого URL-адреса в списке URL-адресов
    threads = []
    for url in urls:
        t = threading.Thread(target=download, args=(url,))
        threads.append(t)

    # Начать загрузку каждого файла одновременно
    for thread in threads:
        thread.start()

    # Дождитесь завершения всех потоков перед выходом из основного потока.
    for thread in threads:
        thread.join()

print('Все загрузки завершены!')
