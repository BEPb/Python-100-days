"""
Python 3.9 Общие модули Python
-Модули, связанные с сервисом выполнения: copy / pickle / sys / ...
-Модули, связанные с математикой: decimal / math / random / ...
-Модуль обработки строк: codecs / re / ...
-Модули, связанные с обработкой файлов: shutil / gzip / ...
- Модули, связанные с сервисом операционной системы: datetime / os / time / logging / io / ...
-Процессные и связанные с потоками модули: multiprocessing / threading / queue
-Модули, связанные с сетевым приложением: ftplib / http / smtplib / urllib / ...
-Модули, связанные с веб-программированием: cgi / webbrowser
-Модуль обработки и кодирования данных: base64 / csv / html.parser / json / xml / ...
Название файла '03.общие_модули.py'

Version: 0.1
Author: Andrej Marinchenko
Date: 2021-11-06
"""

import time  # подключаем модуль работы со временем
import shutil  # подключаем модуль работы с утилитами
import os  # подключаем модуль работы с операционной системой

seconds = time.time()  # определяем сколько сейчас времени, в секундах
print(seconds)  # выводим результат
localtime = time.localtime(seconds)  # определяем сколько сейчас времени, до секунды
print(localtime)  # выводим результат
print(localtime.tm_year)  # выводим результат, только год
print(localtime.tm_mon)  # выводим результат, только месяц
print(localtime.tm_mday)  # выводим результат, только день
asctime = time.asctime(localtime)    # преобразуем результат, в аски формат
print(asctime)  # выводим результат, в аски формате
strtime = time.strftime('%Y-%m-%d %H:%M:%S', localtime)  # преобразуем результат, в свой формат
print(strtime)  # выводим результат

# shutil.copy('/Users/admin/file.py', '/Users/admin/Desktop/file.py')
os.system('ls -l')  # выводит содержимое текущей папки
os.chdir('/Users/admin')  # переходим в указанную папку
os.system('ls -l')  # выводит содержимое текущей папки
os.mkdir('test')  # создает папку тест
