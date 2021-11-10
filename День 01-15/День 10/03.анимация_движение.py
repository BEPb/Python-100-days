"""
Python 3.9 Используйте tkinter для создания графического интерфейса
- анимация движения шара
Название файла '03.анимация_движение.py'

Version: 0.1
Author: Andrej Marinchenko
Date: 2021-11-10
"""

import tkinter
import time

def play_animation():  # Функция воспроизведения эффекта анимации
    canvas.move(oval, 2, 2)
    canvas.update()
    top.after(10, play_animation)


x = 10
y = 10
top = tkinter.Tk()  # создаем объект (окна графического приложения)
# ниже определяем атрибуты объекта (окна приложения)
top.geometry('600x600')  # Установливаем размер окна
top.title('полет шара')  # Установливаем заголовок окна
top.resizable(False, False)  # Установить размер окна в режим - нельзя изменить
top.wm_attributes('-topmost', 1)  # Установить окно вверхнее положение (над другими окнами)


canvas = tkinter.Canvas(top, width=600, height=600, bd=0, highlightthickness=0)# создаем объект рабочей области
# указываем его атрибуты: размер рабочей области,размещение внутри окна top - прижать к верку, отступ
# ниже определяем атрибуты объекта (рабочей области приложения)
canvas.create_rectangle(0, 0, 600, 600, fill='gray')  # рисуем серый квадрат
oval = canvas.create_oval(10, 10, 60, 60, fill='red')  # рисуем круг
canvas.pack()  # определяем менеджер геометрии pack() - все виджеты распологаются вертикально
top.update()  # обновление атрибутов окна
play_animation()  # запуск функции анимации


tkinter.mainloop()  # основной обработчик работы в окне

