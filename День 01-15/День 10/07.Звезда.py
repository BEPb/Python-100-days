"""
Python 3.10 Рисунок многоконечной звезды
Это очень интересный модуль. Он имитирует ползание черепахи по окну, чтобы нарисовать
Название файла '07.Звезда.py'

Version: 0.1
Author: Andrej Marinchenko
Date: 2023-04-09
"""

import turtle  # подключение модуля рисования

turtle.pensize(3)  # устанавливает толщину линии
turtle.penup()  # поднять курсор
turtle.goto(-180, 150)  # переместить курсор
turtle.pencolor('red')  # установить цвет линии
turtle.fillcolor('yellow')  # установить цвет заливки
turtle.pendown()  # опустить курсор
turtle.begin_fill()  # начать зполнение
for _ in range(36):  # в диапазоне до 36
    turtle.forward(200)  # меняется шаг
    turtle.right(170)  # меняется поворот
turtle.end_fill()  # залить фигуру
turtle.mainloop()  # обработчик событий
