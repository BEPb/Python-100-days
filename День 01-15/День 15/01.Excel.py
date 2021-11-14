"""
Python 3.9 создание Excel документа
Название файла '01.Excel.py'

Version: 0.1
Author: Andrej Marinchenko
Date: 2021-11-13
"""
from openpyxl import Workbook
from openpyxl.worksheet.table import Table, TableStyleInfo

workbook = Workbook()
sheet = workbook.active
data = [
    [1001, '323', '33333', '13123456789'],
    [1002, '564', '55543', '13233445566']
]

sheet.append(['12', '13', '14', '15'])
for row in data:
    sheet.append(row)
tab = Table(displayName="Table1", ref="A1:E5")

tab.tableStyleInfo = TableStyleInfo(
    name="TableStyleMedium9", showFirstColumn=False,
    showLastColumn=False, showRowStripes=True, showColumnStripes=True)
sheet.add_table(tab)
workbook.save('./res/97.xlsx')

wb = Workbook()
ws = wb.active

ws['A1'] = 42
ws.append([1, 2, 3])
ws['A2'] = datetime.datetime.now()

wb.save("sample.xlsx")
