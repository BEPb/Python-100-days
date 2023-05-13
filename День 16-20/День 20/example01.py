"""
Python 3.10 Программа преобразователь разрешения изображений находящихся в папке images, создает новые изображения на
 основе существующих, но с разрешением 32х32, 64х64, 128х128 и сохраняет в той же директории
Название файла 'example01.py'

Version: 0.1
Author: Andrej Marinchenko
Date: 2023-05-13
"""
import glob
import os
import time

from concurrent.futures import ThreadPoolExecutor
from threading import Thread

from PIL import Image


# class ThumbnailThread(Thread):
#
#     def __init__(self, infile):
#         self.infile = infile
#         super().__init__()
#
#     def run(self):
#         file, ext = os.path.splitext(self.infile)
#         filename = file[file.rfind('/') + 1:]
#         for size in (32, 64, 128):
#             outfile = f'thumbnails/{filename}_{size}_{size}.png'
#             image = Image.open(self.infile)
#             image.thumbnail((size, size))
#             image.save(outfile, format='PNG')


def gen_thumbnail(infile):
    file, ext = os.path.splitext(infile)
    filename = file[file.rfind('/') + 1:]
    for size in (32, 64, 128):
        # outfile = f'thumbnails/{filename}_{size}_{size}.png'
        outfile = f'{filename}_{size}_{size}.png'
        image = Image.open(infile)
        image.thumbnail((size, size))
        image.save(outfile, format='PNG')


# def main():
#     start = time.time()
#     threads = []
#     for infile in glob.glob('images/*'):
#         # t = Thread(target=gen_thumbnail, args=(infile, ))
#         t = ThumbnailThread(infile)
#         t.start()
#         threads.append(t)
#     for t in threads:
#         t.join()
#     end = time.time()
#     print(f'Время затраченное на выполнение: {end - start} секунд')


def main():
    pool = ThreadPoolExecutor(max_workers=30)
    futures = []
    start = time.time()
    for infile in glob.glob('images/*'):
        # метод отправки - это неблокирующий метод
        # Даже если количество рабочих потоков было израсходовано, метод submit примет отправленную задачу
        future = pool.submit(gen_thumbnail, infile)
        futures.append(future)
    for future in futures:
        # Метод результата - это метод блокировки, если поток еще не завершен
        # Временно невозможно получить результат выполнения потока, код здесь будет заблокирован
        future.result()
    end = time.time()
    print(f'Время затраченное на выполнение: {end - start} секунд')
    # выключение также является неблокирующим методом, но если отправленная задача не была завершена
    # Пул потоков - это завершение работы, которое не перестанет работать, и отправка задачи не будет выполнена и вызовет исключение
    pool.shutdown()


if __name__ == '__main__':
    main()







