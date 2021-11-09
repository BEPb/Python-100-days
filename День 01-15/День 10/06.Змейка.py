"""
Python 3.9 Используйте pygame для создания игры змейка
Название файла '06.Змейка.py'

Version: 0.1
Author: Andrej Marinchenko
Date: 2021-11-10
"""

from abc import ABCMeta, abstractmethod
from enum import Enum, unique
from random import randrange
from threading import Thread

import pygame


class Color(object):
    """цвет"""

    GRAY = (242, 242, 242)
    BLACK = (0, 0, 0)
    GREEN = (0, 255, 0)
    PINK = (255, 20, 147)


@unique
class Direction(Enum):
    """направление"""

    UP = 0
    RIGHT = 1
    DOWN = 2
    LEFT = 3


class GameObject(object, metaclass=ABCMeta):
    """Объекты в игре"""

    def __init__(self, x=0, y=0, color=Color.BLACK):
        """
        Метод инициализации

        : param x: абсцисса
        : param y: ordinate
        : параметр Color: цвет
        """
        self._x = x
        self._y = y
        self._color = color

    @property
    def x(self):
        return self._x

    @property
    def y(self):
        return self._y

    @abstractmethod
    def draw(self, screen):
        """
         рисовать
        :param screen: окно
        """
        pass


class Wall(GameObject):
    """Корпус"""

    def __init__(self, x, y, width, height, color=Color.BLACK):
        """
        Метод инициализации
        : param x: абсцисса
        : param y: ordinate
        : param width: width
        : param height: height
        : параметр цвет: цвет
        """
        super().__init__(x, y, color)
        self._width = width
        self._height = height

    @property
    def width(self):
        return self._width

    @property
    def height(self):
        return self._height

    def draw(self, screen):
        pygame.draw.rect(screen, self._color,
                         (self._x, self._y, self._width, self._height), 4)


class Food(GameObject):
    """еда"""

    def __init__(self, x, y, size, color=Color.PINK):
        """
        Метод инициализации
        : param x: абсцисса
        : param y: ordinate
        : param size: size
        : параметр цвет: цвет
        """
        super().__init__(x, y, color)
        self._size = size
        self._hidden = False

    def draw(self, screen):
        if not self._hidden:
            pygame.draw.circle(screen, self._color,
                               (self._x + self._size // 2, self._y + self._size // 2),
                               self._size // 2, 0)
        self._hidden = not self._hidden


class SnakeNode(GameObject):
    """Узел на змейке"""

    def __init__(self, x, y, size, color=Color.GREEN):
        """
        初Метод инициализации
        : param x: абсцисса
        : param y: ordinate
        : param size: size
        : параметр цвет: цвет
        """
        super().__init__(x, y, color)
        self._size = size

    @property
    def size(self):
        return self._size

    def draw(self, screen):
        pygame.draw.rect(screen, self._color,
                         (self._x, self._y, self._size, self._size), 0)
        pygame.draw.rect(screen, Color.BLACK,
                         (self._x, self._y, self._size, self._size), 1)


class Snake(GameObject):
    """змея"""

    def __init__(self, x, y, size=20, length=5):
        """
       Метод инициализации
        : param x: абсцисса
        : param y: ordinate
        : param size: size
        : param length: начальная длина
        """
        super().__init__()
        self._dir = Direction.LEFT
        self._nodes = []
        self._alive = True
        self._new_dir = None
        for index in range(length):
            node = SnakeNode(x + index * size, y, size)
            self._nodes.append(node)

    @property
    def dir(self):
        return self._dir

    @property
    def alive(self):
        return self._alive

    @property
    def head(self):
        return self._nodes[0]

    def change_dir(self, new_dir):
        """
        изменить направление
        : param new_dir: новое направление
        """
        if new_dir != self._dir and \
                (self._dir.value + new_dir.value) % 2 != 0:
            self._new_dir = new_dir

    def move(self):
        """двигаться"""
        if self._new_dir:
            self._dir, self._new_dir = self._new_dir, None
        snake_dir = self._dir
        x, y, size = self.head.x, self.head.y, self.head.size
        if snake_dir == Direction.UP:
            y -= size
        elif snake_dir == Direction.RIGHT:
            x += size
        elif snake_dir == Direction.DOWN:
            y += size
        else:
            x -= size
        new_head = SnakeNode(x, y, size)
        self._nodes.insert(0, new_head)
        self._nodes.pop()

    def collide(self, wall):
        """
        Ударить стену
        : param wall: забор
        """
        head = self.head
        if head.x < wall.x or head.x + head.size > wall.x + wall.width \
                or head.y < wall.y or head.y + head.size > wall.y + wall.height:
            self._alive = False

    def eat_food(self, food):
        """
        Есть еду
        : param food: еда
        : return: return True, если еда съедена, иначе вернуть False
        """
        if self.head.x == food.x and self.head.y == food.y:
            tail = self._nodes[-1]
            self._nodes.append(tail)
            return True
        return False

    def eat_self(self):
        """Укусить себя"""
        for index in range(4, len(self._nodes)):
            node = self._nodes[index]
            if node.x == self.head.x and node.y == self.head.y:
                self._alive = False

    def draw(self, screen):
        for node in self._nodes:
            node.draw(screen)


def main():

    def refresh():
        """Обновить окно игры"""
        screen.fill(Color.GRAY)
        wall.draw(screen)
        food.draw(screen)
        snake.draw(screen)
        pygame.display.flip()

    def handle_key_event(key_event):
        """Обработка ключевых событий"""
        key = key_event.key
        if key == pygame.K_F2:
            reset_game()
        elif key in (pygame.K_a, pygame.K_w, pygame.K_d, pygame.K_s):
            if snake.alive:
                if key == pygame.K_w:
                    new_dir = Direction.UP
                elif key == pygame.K_d:
                    new_dir = Direction.RIGHT
                elif key == pygame.K_s:
                    new_dir = Direction.DOWN
                else:
                    new_dir = Direction.LEFT
                snake.change_dir(new_dir)

    def create_food():
        """Создать еду"""
        unit_size = snake.head.size
        max_row = wall.height // unit_size
        max_col = wall.width // unit_size
        row = randrange(0, max_row)
        col = randrange(0, max_col)
        return Food(wall.x + unit_size * col, wall.y + unit_size * row, unit_size)

    def reset_game():
        """Сбросить игру"""
        nonlocal food, snake
        food = create_food()
        snake = Snake(250, 290)

    def background_task():
        nonlocal running, food
        while running:
            if snake.alive:
                refresh()
            clock.tick(10)
            if snake.alive:
                snake.move()
                snake.collide(wall)
                if snake.eat_food(food):
                    food = create_food()
                snake.eat_self()

    """
    class BackgroundTask(Thread):

        def run(self):
            nonlocal running, food
            while running:
                if snake.alive:
                    refresh()
                clock.tick(10)
                if snake.alive:
                    snake.move()
                    snake.collide(wall)
                    if snake.eat_food(food):
                        food = create_food()
                    snake.eat_self()
    """

    wall = Wall(10, 10, 600, 600)
    snake = Snake(250, 290)
    food = create_food()
    pygame.init()
    screen = pygame.display.set_mode((620, 620))
    pygame.display.set_caption('змейка')
    # Создайте часы, которые контролируют количество кадров в секунду в игре
    clock = pygame.time.Clock()
    running = True
    # Запускаем фоновый поток, отвечающий за обновление окна и позволяющий змейке двигаться
    # BackgroundTask().start()
    Thread(target=background_task).start()
    # Обработка цикла сообщений о событиях
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                handle_key_event(event)
    pygame.quit()


if __name__ == '__main__':
    main()
