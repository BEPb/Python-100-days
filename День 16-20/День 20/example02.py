"""
Python 3.10 Программа преобразователь разрешения изображений находящихся в папке images, создает новые изображения на
 основе существующих, но с разрешением 32х32, 64х64, 128х128 и сохраняет в той же директории
Название файла 'example02.py'

Version: 0.1
Author: Andrej Marinchenko
Date: 2023-05-13
"""
import glob
import os
import time

from threading import Thread
from PIL import Image


class ThumbnailThread(Thread):

    def __init__(self, infile):
        self.infile = infile
        super().__init__()

    def run(self):
        file, ext = os.path.splitext(self.infile)
        filename = file[file.rfind('/') + 1:]
        for size in (32, 64, 128):
            outfile = f'{filename}_{size}_{size}.png'
            image = Image.open(self.infile)
            image.thumbnail((size, size))
            image.save(outfile, format='PNG')


def main():
    start = time.time()
    threads = []
    for infile in glob.glob('images/*'):
        t = ThumbnailThread(infile)
        t.start()
        threads.append(t)
    for t in threads:
        t.join()
    end = time.time()
    print(f'Время затраченное на выполнение: {end - start} секунд')



if __name__ == '__main__':
    main()







