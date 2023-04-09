"""
Python 3.10 Игра в мячики, где после нажатия мышкой по окну игры появляется мяч произвольного размера, который при
столкновении съедает шар меньшего размера и увеличивает свой размер. Все мячи отпрыгивают от стенок по закону
равенства угла падения углу отражения.
Название файла '04.игра_мячи.py'
7xz8777
Version: 0.1
Author: Andrej Marinchenko
Date: 2023-04-09
"""

from enum import Enum, unique  # подключаем модуль перечисления значений и работы с ними
from math import sqrt  # подключть функцию квадратного корня
from random import randint  # подключить функцию генерацию случайных чисел

import pygame  # подключить модуль создания игр


@unique
class Color(Enum):  # создаем класс цвета (наследуем от Enum)
    """цвет"""
    # задаем цвета в rgb-формате
    RED = (255, 0, 0)
    GREEN = (0, 255, 0)
    BLUE = (0, 0, 255)
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    GRAY = (242, 242, 242)

    @staticmethod  # статический метод
    def random_color():  # генерирует случайный цвет
        """Получить случайные цвета"""
        r = randint(0, 255)  # генерирует случайное число от 0 до 255 и присваивает значению красного спектра
        g = randint(0, 255)  # генерирует случайное число от 0 до 255 и присваивает значению зеленого спектра
        b = randint(0, 255)  # генерирует случайное число от 0 до 255 и присваивает значению синего спектра
        return (r, g, b)  # возвращает цвет, на основе 3-х случайных цветовых спектров


class Ball(object):  # создаем класс мяча
    """мяч"""

    def __init__(self, x, y, radius, sx, sy, color=Color.RED):  # инициализация класса  (на входе аргументы
        # координат, радиуса круга, смещение по осям и цвет (по умолчанию красный))
        """Метод инициализации"""
        # далее определяем атрибуты класса из полученнных аргументов
        self.x = x
        self.y = y
        self.radius = radius
        self.sx = sx
        self.sy = sy
        self.color = color
        self.alive = True  # отрибут живой = истина

    def move(self, screen):  # метод движения
        """двигаться"""
        # переопределяет новое положение координат шара на основе смещения по осям
        self.x += self.sx
        self.y += self.sy

        # определяем изменение направления движения в случае достижения стенок окна
        if self.x - self.radius <= 0 or self.x + self.radius >= screen.get_width():  # по оси х
            self.sx = -self.sx  # смещение по оси х меняет знак, тем самым шар отбивается от стенки
        if self.y - self.radius <= 0 or self.y + self.radius >= screen.get_height():  # по оси у
            self.sy = -self.sy  # смещение по оси х меняет знак, тем самым шар отбивается от стенки

    def eat(self, other):  # метод поедания других мячей
        """Ешьте другие мячи"""
        if self.alive and other.alive and self != other:  # если оцениваемые мячи живы
            dx, dy = self.x - other.x, self.y - other.y  # вычисляем проекцию между центрами мячей
            distance = sqrt(dx ** 2 + dy ** 2)  # вычисляем растояние между мячами
            if distance < self.radius + other.radius \
                    and self.radius > other.radius:  # если сумма радиусов меньше дистанции между мячами
                other.alive = False  # то меняем статус мяча на не живой
               	self.radius = self.radius + int(other.radius * 0.146)  # увеличиваем радиус мяча в зависимости от
            # радиуса поглащенного мяча

    def draw(self, screen):  # метод рисования мяча
        """Нарисуйте мяч на окне"""
        pygame.draw.circle(screen, self.color,
                           (self.x, self.y), self.radius, 0)  # рисуем мяч


def main():  # главная функция
    # Определить контейнер, используемый для хранения всех шаров
    balls = []
    # Инициализировать импортированный модуль pygame
    pygame.init()
    # Инициализировать окно для отображения и установить размер окна
    screen = pygame.display.set_mode((800, 600))
    print(screen.get_width())
    print(screen.get_height())
    # Установить заголовок текущего окна
    pygame.display.set_caption('большой мяч ест маленький мяч')
    # Определить переменные для представления положения мяча на экране
    x, y = 50, 50
    running = True

    # Открываем цикл обработки событий
    while running:
        # Получить события из очереди сообщений и обработать их
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                x, y = event.pos
                radius = randint(10, 100)
                sx, sy = randint(-10, 10), randint(-10, 10)
                color = Color.random_color()
                ball = Ball(x, y, radius, sx, sy, color)
                balls.append(ball)
        screen.fill((255, 255, 255))
        for ball in balls:
            if ball.alive:
                ball.draw(screen)
            else:
                balls.remove(ball)
        pygame.display.flip()

        # Менять положение шара каждые 50 миллисекунд и обновлять окно
        pygame.time.delay(50)
        for ball in balls:
            ball.move(screen)
            for other in balls:
                ball.eat(other)


if __name__ == '__main__':  # если запущена эта программа
    main()  # выполнить главную функцию
