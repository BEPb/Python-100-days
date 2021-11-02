"""
Нарисуйте национальный флаг с помощью модуля Python turtle
"""
import turtle  # импортируем модуль для рисования "черепаха"


def draw_rectangle(x, y, width, height):  # имя функции и принимаемые для обработки переменные
    """Рисуем прямоугольник"""
    turtle.goto(x, y)  # перемещаем курсор на позицию x, y
    turtle.pencolor('red')  # определяем цвет контура рисования
    turtle.fillcolor('red')  # определяем цвет заливки
    turtle.begin_fill()  # приступить к заполнению
    for i in range(2):  # цикл от 1-го до 2-х
        turtle.forward(width)
        turtle.left(90)
        turtle.forward(height)
        turtle.left(90)
    turtle.end_fill()  # завершить заполнение, заливает указанные линии цветом


def draw_star(x, y, radius):
    """Рисуем пятиконечную звезду"""
    turtle.setpos(x, y)  # определяем место курсора 1-я точка пятиконечной звезды
    pos1 = turtle.pos()  # запоминаем 1-ю точку пятиконечной звезды
    turtle.circle(-radius, 72)
    pos2 = turtle.pos()  # запоминаем 2-ю точку пятиконечной звезды
    turtle.circle(-radius, 72)
    pos3 = turtle.pos()  # запоминаем 3-ю точку пятиконечной звезды
    turtle.circle(-radius, 72)
    pos4 = turtle.pos()  # запоминаем 4-ю точку пятиконечной звезды
    turtle.circle(-radius, 72)
    pos5 = turtle.pos()  # запоминаем 5-ю точку пятиконечной звезды
    turtle.color('yellow', 'yellow')  # определяем цвет звезды контур и заливка
    turtle.begin_fill()  # приступить к заполнению, далее рисуем линии между вершинами звезды
    turtle.goto(pos3)
    turtle.goto(pos1)
    turtle.goto(pos4)
    turtle.goto(pos2)
    turtle.goto(pos5)
    turtle.end_fill()  # завершить заполнение, заливает указанные линии цветом


def main():
    """Основная программа"""
    turtle.speed(12)  # определяем скорость
    turtle.penup()  # поднимаем курсор
    x, y = -270, -180  # задаем координаты

    # Рисуем основную часть флага
    width, height = 540, 360  # задаем ширину и высоту флага
    draw_rectangle(x, y, width, height)  # запускаем функцию рисования флага, в которую передаем начальные
    # координаты, ширину и высоту

    # Рисуем большую звезду
    pice = 22
    center_x, center_y = x + 5 * pice, y + height - pice * 5
    turtle.goto(center_x, center_y)
    turtle.left(90)
    turtle.forward(pice * 3)
    turtle.right(90)
    draw_star(turtle.xcor(), turtle.ycor(), pice * 3)  # запускаем функцию рисования звезды


    x_poses, y_poses = [10, 12, 12, 10], [2, 4, 7, 9]

    # Рисуем 4 маленьких звездочки
    for x_pos, y_pos in zip(x_poses, y_poses):
        turtle.goto(x + x_pos * pice, y + height - y_pos * pice)
        turtle.left(turtle.towards(center_x, center_y) - turtle.heading())
        turtle.forward(pice)
        turtle.right(90)
        draw_star(turtle.xcor(), turtle.ycor(), pice)
    # убираем курсор для рисования (черепаху)
    turtle.ht()
    # Показать окно рисования
    turtle.mainloop()


if __name__ == '__main__':
    main()