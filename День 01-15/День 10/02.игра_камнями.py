"""
Python 3.9 ИИспользуйте tkinter для создания графического интерфейса
-Используйте холст для рисования
-Обработка событий мыши
Название файла '02.игра_камнями.py'

Version: 0.1
Author: Andrej Marinchenko
Date: 2021-11-10
"""

import tkinter


def mouse_evt_handler(evt=None):
    row = round((evt.y - 20) / 40)
    col = round((evt.x - 20) / 40)
    pos_x = 40 * col
    pos_y = 40 * row
    canvas.create_oval(pos_x, pos_y, 40 + pos_x, 40 + pos_y, fill='black')


top = tkinter.Tk()
# Установить размер окна
top.geometry('620x620')
# Установить заголовок окна
top.title('игра камнями')
# Установить размер окна нельзя изменить
top.resizable(False, False)
# Установить окно вверх
top.wm_attributes('-topmost', 1)
canvas = tkinter.Canvas(top, width=600, height=600, bd=0, highlightthickness=0)
canvas.bind('<Button-1>', mouse_evt_handler)
canvas.create_rectangle(0, 0, 600, 600, fill='yellow', outline='white')
for index in range(15):
    canvas.create_line(20, 20 + 40 * index, 580, 20 + 40 * index, fill='black')
    canvas.create_line(20 + 40 * index, 20, 20 + 40 * index, 580, fill='black')
canvas.create_rectangle(15, 15, 585, 585, outline='black', width=4)
canvas.pack()
tkinter.mainloop()

# Пожалуйста, подумайте, как инкапсулировать приведенный выше код с идеями объектно-ориентированного программирования
