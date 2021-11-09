"""
Python 3.9 Рисунок многоконечной звезды
Это очень интересный модуль. Он имитирует ползание черепахи по окну, чтобы нарисовать
Название файла '07.Звезда.py'

Version: 0.1
Author: Andrej Marinchenko
Date: 2021-11-10
"""

import turtle

turtle.pensize(3)
turtle.penup()
turtle.goto(-180, 150)
turtle.pencolor('red')
turtle.fillcolor('yellow')
turtle.pendown()
turtle.begin_fill()
for _ in range(36):
    turtle.forward(200)
    turtle.right(170)
turtle.end_fill()
turtle.mainloop()
