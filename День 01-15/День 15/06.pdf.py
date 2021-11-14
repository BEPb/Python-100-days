"""
Python 3.9 чтение pdf документа
Название файла '06.pdf.py'

Version: 0.1
Author: Andrej Marinchenko
Date: 2021-11-13
"""

from PyPDF2 import PdfFileReader

with open('./res/Docker.pdf', 'rb') as f:
    reader = PdfFileReader(f, strict=False)
    print(reader.numPages)
    if reader.isEncrypted:
        reader.decrypt('')
    current_page = reader.getPage(5)
    print(current_page)
    print(current_page.extractText())
