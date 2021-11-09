"""
Python 3.9 Используйте tkinter для создания графического интерфейса
-анимация движения шара
Название файла '03.анимация_движение.py'

Version: 0.1
Author: Andrej Marinchenko
Date: 2021-11-10
"""

import tkinter
import time


# Функция для воспроизведения эффекта анимации
def play_animation():
    canvas.move(oval, 2, 2)
    canvas.update()
    top.after(50, play_animation)


x = 10
y = 10
top = tkinter.Tk()
top.geometry('600x600')
top.title('动画效果')
top.resizable(False, False)
top.wm_attributes('-topmost', 1)
canvas = tkinter.Canvas(top, width=600, height=600, bd=0, highlightthickness=0)
canvas.create_rectangle(0, 0, 600, 600, fill='gray')
oval = canvas.create_oval(10, 10, 60, 60, fill='red')
canvas.pack()
top.update()
play_animation()
tkinter.mainloop()

# Пожалуйста, подумайте, как заставить мяч отскочить назад, когда он достигнет границы экрана
# Пожалуйста, подумайте, как инкапсулировать приведенный выше код с идеями объектно-ориентированного программирования
