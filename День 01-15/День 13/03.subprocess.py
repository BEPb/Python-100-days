"""
Python 3.9 Создайте процесс для вызова других программ
Название файла '03.subprocess.py'

Version: 0.1
Author: Andrej Marinchenko
Date: 2021-11-11
"""

import subprocess
import sys

def main():
    # Получить параметры командной строки через sys.argv
    if len(sys.argv) > 1:
        # Первый параметр командной строки - это сама программа, поэтому начнем со второго
        for index in range(1, len(sys.argv)):
            try:
                # Запуск подпроцесса через функцию вызова модуля подпроцесса
                status = subprocess.call(sys.argv[index])
            except FileNotFoundError:
                print('Невозможно выполнить команду %s ' % sys.argv[index])
    else:
        print('Пожалуйста, используйте параметры командной строки, чтобы указать выполняемый процесс')


if __name__ == '__main__':
    main()
