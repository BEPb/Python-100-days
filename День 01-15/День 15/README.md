[Вернуться на главную](https://github.com/BEPb/Python-100-days)


## Обработка изображений и офисных документов

Программы для обработки изображений и офисных документов часто появляются в реальной разработке. Хотя в стандартной 
библиотеке Python нет модуля, который напрямую поддерживает эти операции, мы можем выполнять эти операции с помощью 
сторонних модулей в экосистеме Python.

### Операции с изображением

### Знания, связанные с компьютерными изображениями 
#### Цвет
Если у вас есть опыт рисования красками, вы должны знать, что вы можете получить другие цвета, смешивая красную, 
желтую и синюю краски. Фактически, эти три цвета - это то, что мы называем тремя основными цветами искусства.  В 
компьютере мы можем наложить три цвета: красный, зеленый и синий в 
разных пропорциях, чтобы объединить их в другие цвета, поэтому мы обычно выражаем цвет как значение RGB или 
значение RGBA (где A представляет альфа-канал, который определяет пиксели, проходящие через изображение, то есть 
прозрачность).

   | цвет  |        RGBA Значение        |  цвет  |       RGBA Значение       |
   | :---: | :------------------: | :----: | :----------------: |
   | White | (255, 255, 255, 255) |  Red   |  (255, 0, 0, 255)  |
   | Green |   (0, 255, 0, 255)   |  Blue  |  (0, 0, 255, 255)  |
   | Gray  | (128, 128, 128, 255) | Yellow | (255, 255, 0, 255) |
   | Black |    (0, 0, 0, 255)    | Purple | (128, 0, 128, 255) |

#### Пиксели
Для изображения, представленного последовательностью чисел, самая маленькая единица - это маленький квадрат одного 
цвета на изображении. Эти маленькие квадраты имеют четкое положение и значение цвета, а цвет и 
положение этих маленьких квадратов определяют окончательный вид изображения, они являются неделимыми единицами, 
которые мы обычно называем пикселями. Каждое изображение содержит определенное количество пикселей, которые 
определяют размер изображения на экране.

#### Управляйте изображениями с помощью подушки Pillow

Pillow это ответвление, разработанное на основе известной библиотеки обработки изображений Python PIL. С помощью 
Pillow можно реализовать различные операции, такие как сжатие и обработка изображений. Вы можете использовать 
следующую команду для установки Pillow.

```Shell
pip install pillow
```

Самым важным в Pillow является класс Image, который необходимо использовать для чтения и обработки изображений.

```Python
>>> from PIL import Image
>>>
>>> image = Image.open('./res/guido.jpg')
>>> image.format, image.size, image.mode
('JPEG', (500, 750), 'RGB')
>>> image.show()
```

1. Обрезать изображение

```Python
>>> image = Image.open('./res/guido.jpg')
>>> rect = 80, 20, 310, 360
>>> image.crop(rect).show()
```


2. Создать миниатюру

```Python
>>> image = Image.open('./res/guido.jpg')
>>> size = 128, 128
>>> image.thumbnail(size)
>>> image.show()
```


3. Масштабировать и вставлять изображения

```Python
>>> image1 = Image.open('./res/luohao.png')
>>> image2 = Image.open('./res/guido.jpg')
>>> rect = 80, 20, 310, 360
>>> guido_head = image2.crop(rect)
>>> width, height = guido_head.size
>>> image1.paste(guido_head.resize((int(width / 1.5), int(height / 1.5))), (172, 40))
```


4. Повернуть и перевернуть

```Python
>>> image = Image.open('./res/guido.png')
>>> image.rotate(180).show()
>>> image.transpose(Image.FLIP_LEFT_RIGHT).show()
```


5. Рабочие пиксели

```Python
>>> image = Image.open('./res/guido.jpg')
>>> for x in range(80, 310):
...     for y in range(20, 360):
...         image.putpixel((x, y), (128, 128, 128))
... 
>>> image.show()
   ```

6. Эффект фильтра

```Python
>>> from PIL import Image, ImageFilter
>>>
>>> image = Image.open('./res/guido.jpg')
>>> image.filter(ImageFilter.CONTOUR).show()
```


### Обработка таблиц Excel

Модуль openpyxl Python позволяет нам читать и изменять электронные таблицы Excel в программах на Python. Поскольку 
 Microsoft использует формат файлов с Office 2007, это делает Office Excel, LibreOffice Calc и OpenOffice 
Calc полностью совместимыми, что означает, что модуль openpyxl также может обрабатывать электронные таблицы 
генерируется из этого программного обеспечения.

```Python
import datetime

from openpyxl import Workbook

wb = Workbook()
ws = wb.active

ws['A1'] = 42
ws.append([1, 2, 3])
ws['A2'] = datetime.datetime.now()

wb.save("sample.xlsx")
```

### Обработка документов Word

Используя модуль python-docx, Python может создавать и изменять документы Word. Конечно, документы Word здесь - это 
не просто документы с расширением docx, созданные программным обеспечением Microsoft Office. LibreOffice Writer и 
OpenOffice Writer - это бесплатное программное обеспечение для обработки текста.

```Python
"""
Python 3.10 создание Word документа
Название файла '03.Word.py'

Version: 0.1
Author: Andrej Marinchenko
Date: 2023-04-27
"""
from docx import Document
from docx.shared import Inches

document = Document()

document.add_heading('Document Title', 0)

p = document.add_paragraph('A plain paragraph having some ')
p.add_run('bold').bold = True
p.add_run(' and some ')
p.add_run('italic.').italic = True

document.add_heading('Heading, level 1', level=1)
document.add_paragraph('Intense quote', style='Intense Quote')

document.add_paragraph(
    'first item in unordered list', style='List Bullet'
)
document.add_paragraph(
    'first item in ordered list', style='List Number'
)

document.add_picture('monty-truth.png', width=Inches(1.25))

records = (
    (3, '101', 'Spam'),
    (7, '422', 'Eggs'),
    (4, '631', 'Spam, spam, eggs, and spam')
)

table = document.add_table(rows=1, cols=3)
hdr_cells = table.rows[0].cells
hdr_cells[0].text = 'Qty'
hdr_cells[1].text = 'Id'
hdr_cells[2].text = 'Desc'
for qty, id, desc in records:
    row_cells = table.add_row().cells
    row_cells[0].text = str(qty)
    row_cells[1].text = id
    row_cells[2].text = desc

document.add_page_break()

document.save('demo.docx')
```


[Вернуться на главную](https://github.com/BEPb/Python-100-days)
