"""
Python 3.9 Игра в мячики, где после нажатия мышкой по окну игры появляется мяч произвольного размера, который при
столкновении съедает шар меньшего размера и увеличивает свой размер. Все мячи отпрыгивают от стенок по закону
равенства угла падения углу отражения.
Название файла '04.игра_мячи.py'

Version: 0.1
Author: Andrej Marinchenko
Date: 2021-11-10
"""

from enum import Enum, unique
from math import sqrt
from random import randint

import pygame


@unique
class Color(Enum):
    """цвет"""

    RED = (255, 0, 0)
    GREEN = (0, 255, 0)
    BLUE = (0, 0, 255)
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    GRAY = (242, 242, 242)

    @staticmethod
    def random_color():
        """Получить случайные цвета"""
        r = randint(0, 255)
        g = randint(0, 255)
        b = randint(0, 255)
        return (r, g, b)


class Ball(object):
    """мяч"""

    def __init__(self, x, y, radius, sx, sy, color=Color.RED):
        """Метод инициализации"""
        self.x = x
        self.y = y
        self.radius = radius
        self.sx = sx
        self.sy = sy
        self.color = color
        self.alive = True

    def move(self, screen):
        """двигаться"""
        self.x += self.sx
        self.y += self.sy
        if self.x - self.radius <= 0 or self.x + self.radius >= screen.get_width():
            self.sx = -self.sx
        if self.y - self.radius <= 0 or self.y + self.radius >= screen.get_height():
            self.sy = -self.sy

    def eat(self, other):
        """Ешьте другие мячи"""
        if self.alive and other.alive and self != other:
            dx, dy = self.x - other.x, self.y - other.y
            distance = sqrt(dx ** 2 + dy ** 2)
            if distance < self.radius + other.radius \
                    and self.radius > other.radius:
                other.alive = False
               	self.radius = self.radius + int(other.radius * 0.146)

    def draw(self, screen):
        """Нарисуйте мяч на окне"""
        pygame.draw.circle(screen, self.color,
                           (self.x, self.y), self.radius, 0)


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
    # Открываем цикл обработки событий для обработки происходящих событий
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
