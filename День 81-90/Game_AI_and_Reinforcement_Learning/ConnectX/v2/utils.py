"""
Python 3.9 программа утилит (обработки начального тестового датасета из 1000 игр, оценки результата игры)
программа на Python по изучению обучения с подкреплением - Reinforcement Learning
Название файла connect4_game.py

Version: 0.1
Author: Andrej Marinchenko
Date: 2021-12-22
"""

class dotdict(dict):
    def __getattr__(self, name):
        try:
            return self[name]
        except KeyError:
            raise AttributeError(name)

# функция определения победа\пройгрыш\ничья
def win_loss_draw(score):
    if score > 0:
        return 'win'
    if score < 0:
        return 'loss'
    return 'draw'

# split one list to multiple lists
"""
разделить один список на несколько списков
"""
split_group = lambda the_list, group_size: zip(*(iter(the_list), ) * group_size)

import numpy as np   # базовые методы для манипуляции с большими массивами и матрицами
import json   # работа с файлами формата json
from connect4_game import Connect4Game  # подключаем собственный модуль
# Connect4 Game - класс, реализующий общий интерфейс игры alpha-zero. Используйте 1 для player1 и -1 для player2.

def get_test_dataset():  # функция обработки тестового датасета
    game = Connect4Game()  # копируем класс
    test_dataset = []  # создаем пустой список
    # with open("refmoves1k_kaggle") as f:
    "переменной f присвоим датасет из json файла refmoves1k_kaggle"
    number_str = 1
    with open("/home/user/PycharmProjects/Python-100-days/Game_AI_and_Reinforcement_Learning/ConnectX/v2/refmoves1k_kaggle") as f:
        print('Чтение исходного файла данных')
        for line in f:  # проводим обработку датасета построчно
            data = json.loads(line)  # создаем датафрем равный одной строке
            print("Обработка одной игры (строки датасета) - %s" % number_str)
            number_str += 1
            board = data["board"]  # из датафрейма берем данные доски
            board = np.reshape(board, game.getBoardSize()).astype(int)
            board[np.where(board == 2)] = -1

            # find out how many moves are played to set the correct mark.
            "узнайте, сколько ходов сделано, чтобы поставить правильную отметку."
            ply = len([x for x in data["board"] if x > 0])
            if ply & 1:
                player = -1
            else:
                player = 1

            test_dataset.append({
                'board': board,
                'player': player,
                'move_score': data['move score'],
            })
    return test_dataset
