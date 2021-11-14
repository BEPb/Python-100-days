"""
Python 3.9 чтение, преобразование, сохранение pillow документа
Название файла '05.pillow.py'

Version: 0.1
Author: Andrej Marinchenko
Date: 2021-11-13
"""
from PIL import Image

img = Image.open('./res/guido.jpg')
print(img.size)
print(img.format)
print(img.format_description)
img.save('./res/guido.png')

img2 = Image.open('./res/guido.png')
img3 = img2.crop((335, 435, 430, 615))
for x in range(4):
    for y in range(5):
        img2.paste(img3, (95 * y , 180 * x))
img2.resize((img.size[0] // 2, img.size[1] // 2))
img2.rotate(90)
img2.save('./res/guido2.png')
