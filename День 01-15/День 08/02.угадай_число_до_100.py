"""
Python 3.9 Объектно-ориентированная версия игры в угадывание чисел
Название файла '02.угадай_число_до_100.py'

Version: 0.1
Author: Andrej Marinchenko
Date: 2021-11-08
"""

from random import randint


class GuessMachine(object):

    def __init__(self):
        self._answer = None
        self._counter = None
        self._hint = None

    def reset(self):
        self._answer = randint(1, 100)
        self._counter = 0
        self._hint = None

    def guess(self, your_answer):
        self._counter += 1
        if your_answer > self._answer:
            self._hint = 'меньше'
        elif your_answer < self._answer:
            self._hint = 'больше'
        else:
            self._hint = 'Поздравляю, вы угадали'
            return True
        return False

    @property
    def counter(self):
        return self._counter

    @property
    def hint(self):
        return self._hint


if __name__ == '__main__':
    gm = GuessMachine()
    play_again = True
    while play_again:
        game_over = False
        gm.reset()
        while not game_over:
            your_answer = int(input('Пожалуйста, введите '))
            game_over = gm.guess(your_answer)
            print(gm.hint)
        if gm.counter > 7:
            print('«Баланс IQ недостаточен!»')
        play_again = input('Играть снова? (да | нет)') == 'да'
