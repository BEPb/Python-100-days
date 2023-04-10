"""
Python 3.10 Чтение и запись двоичных файлов
Название файла '08.чтение_запись_избражений.py'

Version: 0.1
Author: Andrej Marinchenko
Date: 2023-04-09
"""
import base64

with open('96.mm.jpg', 'rb') as f:
    data = f.read()
    # print(type(data))
    # print(data)
    print('Количество байтов:', len(data))
    # Обработать картинку в кодировке BASE-64
    print(base64.b64encode(data))

with open('girl.jpg', 'wb') as f:
    f.write(data)
print('Запись завершена!')
