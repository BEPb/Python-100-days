"""
Python 3.10 чтение pdf документа
Название файла '06.pdf.py'

Version: 0.1
Author: Andrej Marinchenko
Date: 2023-04-27
"""

from PyPDF2 import PdfReader

with open('./res/rukovodstvo.pdf', 'rb') as f:
    reader = PdfReader(f, strict=False)
    print(len(reader.pages))
    if reader.is_encrypted:
        reader.decrypt('')
    current_page = reader.pages[5]
    print(current_page)
    print(current_page.extract_text())
