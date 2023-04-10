"""
Python 3.10 Прочитать данные из текстового файла
Название файла '05.чтение_текст_файла.py'

Version: 0.1
Author: Andrej Marinchenko
Date: 2023-04-09
"""

import time


def main():
    # Прочитать сразу все содержимое файла
    with open('99.txt', 'r', encoding='utf-8') as f:
        print(f.read())

    # Прочитать построчно через цикл for-in
    with open('99.txt', mode='r') as f:
        for line in f:
            print(line, end='')
            time.sleep(0.5)
    print()

    # Прочитать файл и прочитать его построчно в список
    with open('99.txt') as f:
        lines = f.readlines()
    print(lines)
    

if __name__ == '__main__':
    main()
