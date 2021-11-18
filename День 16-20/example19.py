"""
Python 3.9
Масштабируемая производительность системы
-Вертикальное расширение-Увеличение производительности обработки одного узла
-Горизонтальное расширение-превращение одного узла в несколько узлов (разделение чтения-записи / распределенный кластер)
Параллельное программирование - ускорение выполнения программы / улучшение взаимодействия с пользователем
Трудоемкие задачи выполняются максимально независимо, не блокируют другие части кода.
- Многопоточность
1. Создайте объект Thread, чтобы указать атрибуты target и args, и запустите поток с помощью метода start.
2. Наследуйте класс Thread и переопределите метод run, чтобы определить задачи, выполняемые потоком.
3. Создайте объект пула потоков ThreadPoolExecutor и отправьте задачу для выполнения через submit.
Третий способ может получить результат выполнения потока в будущем через метод result объекта Future
Вы также можете использовать метод done, чтобы определить, закончился ли поток
- мульти-прогресс
-Асинхронный ввод / вывод
Название файла 'example19.py'

Version: 0.1
Author: Andrej Marinchenko
Date: 2021-11-18
"""
import glob
import os
import time

from concurrent.futures import ThreadPoolExecutor
from threading import Thread

from PIL import Image


# class ThumbnailThread(Thread):

#     def __init__(self, infile):
#         self.infile = infile
#         super().__init__()

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
        outfile = f'thumbnails/{filename}_{size}_{size}.png'
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
#     print(f'耗时: {end - start}秒')


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
    print(f'耗时: {end - start}秒')
    # выключение также является неблокирующим методом, но если отправленная задача не была завершена
    # Пул потоков - это завершение работы, которое не перестанет работать, и отправка задачи не будет выполнена и вызовет исключение
    pool.shutdown()


if __name__ == '__main__':
    main()







