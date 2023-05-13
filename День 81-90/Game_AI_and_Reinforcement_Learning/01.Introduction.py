# Introduction
# from learntools.core import binder
# binder.bind(globals())
# from learntools.game_ai.ex1 import *

# 1) Более умный агент
# Мы можем улучшить производительность, не изобретая сложной стратегии, просто выбрав выигрышный ход, если он доступен.
#
# В этом упражнении вы создадите агент, который:
# выбирает выигрышный ход, если он доступен. (Если есть более одного хода, который позволяет агенту выиграть игру,
# агент может выбрать любой из них.)
# В противном случае он должен выбрать случайный ход.
# Чтобы помочь вам с этой целью, мы предоставляем несколько вспомогательных функций в ячейке кода ниже.

import numpy as np

# Gets board at next step if agent drops piece in selected column
# Получает доску на следующем шаге, если агент уронит фигуру в выбранном столбце
def drop_piece(grid, col, piece, config):
    next_grid = grid.copy()
    for row in range(config.rows-1, -1, -1):
        if next_grid[row][col] == 0:
            break
    next_grid[row][col] = piece
    return next_grid

# Returns True if dropping piece in column results in game win
# Возвращает True, если выпадение фишки в столбце приводит к победе в игре
def check_winning_move(obs, config, col, piece):
    # Convert the board to a 2D grid
    # Преобразовать плату в 2D сетку
    grid = np.asarray(obs.board).reshape(config.rows, config.columns)
    next_grid = drop_piece(grid, col, piece, config)
    # horizontal
    # по горизонтали
    for row in range(config.rows):
        for col in range(config.columns-(config.inarow-1)):
            window = list(next_grid[row,col:col+config.inarow])
            if window.count(piece) == config.inarow:
                return True
    # vertical
    # вертикальный
    for row in range(config.rows-(config.inarow-1)):
        for col in range(config.columns):
            window = list(next_grid[row:row+config.inarow,col])
            if window.count(piece) == config.inarow:
                return True
    # positive diagonal
    # положительная диагональ
    for row in range(config.rows-(config.inarow-1)):
        for col in range(config.columns-(config.inarow-1)):
            window = list(next_grid[range(row, row+config.inarow), range(col, col+config.inarow)])
            if window.count(piece) == config.inarow:
                return True
    # negative diagonal
    # отрицательная диагональ
    for row in range(config.inarow-1, config.rows):
        for col in range(config.columns-(config.inarow-1)):
            window = list(next_grid[range(row, row-config.inarow, -1), range(col, col+config.inarow)])
            if window.count(piece) == config.inarow:
                return True
    return False

# Функция check_winning_move() принимает четыре обязательных аргумента: первые два (obs и config) должны быть вам
# знакомы, и:
#
# col - любой допустимый ход
# piece (фишка) - это либо знак агента, либо его оппонента.
# Функция возвращает True, если бросок фишки в указанном столбце приводит к выигрышу в игре (либо для агента,
# либо для его противника), в противном случае возвращает False. Чтобы проверить, сможет ли агент выиграть на
# следующем ходу, вы должны установить piece = obs.mark.
#
# Для выполнения этого упражнения вам необходимо определить agent_q1() в ячейке кода ниже. Для этого вам
#  рекомендуется использовать функцию check_winning_move ().
#
# Функция drop_piece () (определенная в ячейке кода выше) вызывается в функции check_winning_move (). Не стесняйтесь
# изучать детали, но вам не понадобится детальное понимание для решения упражнения.

# Подсказка: используйте функцию check_winning_move () и установите piece = obs.mark. Вы можете проверить,
# может ли агент выиграть игру, опустив свой кусок в определенный столбец, указав этот столбец в качестве аргумента
#  функции col.
import random

def agent_q1(obs, config):
    valid_moves = [col for col in range(config.columns) if obs.board[col] == 0]
    for col in valid_moves:
        if check_winning_move(obs, config, col, obs.mark):
            return col
    return random.choice(valid_moves)

# Строки ниже дадут вам подсказку или код решения.
def agent_q2(obs, config):
    valid_moves = [col for col in range(config.columns) if obs.board[col] == 0]
    for col in valid_moves:
        if check_winning_move(obs, config, col, obs.mark):
            return col
    for col in valid_moves:
        if check_winning_move(obs, config, col, obs.mark%2+1):
            return col
    return random.choice(valid_moves)

# 3) Заглядывая в будущее
# До сих пор вы закодировали агента, который всегда выбирает выигрышный ход, если он доступен. И он также может
# блокировать победу противника.
#
# Вы могли ожидать, что этот агент должен работать достаточно хорошо! Но как все же возможно, что он все еще может
# проиграть игру?
# Решение: агент все равно может проиграть игру, если
#
# противник установил доску так, чтобы он мог выиграть в следующий ход, уронив диск в любой из 2 или более столбцов,
# или
# Единственный ход, доступный агенту, - это ход, когда оппонент, разыграв его, может выиграть следующим ходом.


# 4) Игра против агента
# Измените функцию my_agent() ниже, чтобы создать свой собственный агент. Не стесняйтесь копировать агента, созданного вами выше.
#
# Обратите внимание, что вам нужно будет включить все необходимые импортные и вспомогательные функции. Чтобы увидеть
# пример того, как это будет выглядеть с первым агентом, созданным вами в упражнении, взгляните на этот блокнот.
def my_agent(obs, config):
    # Your code here: Amend the agent!
    import random
    valid_moves = [col for col in range(config.columns) if obs.board[col] == 0]
    for col in valid_moves:
        if check_winning_move(obs, config, col, obs.mark):
            return col
    for col in valid_moves:
        if check_winning_move(obs, config, col, obs.mark % 2 + 1):
            return col

    return random.choice(valid_moves)


# Запустите следующую ячейку кода, чтобы сыграть раунд игры против агента. Чтобы выбрать ход, щелкните на игровом
# экране в столбце, куда вы хотите поместить диск.
# После завершения игры вы можете повторно запустить ячейку кода, чтобы играть снова!
from kaggle_environments import evaluate, make, utils

env = make("connectx", debug=True)
env.play([my_agent, None], width=500, height=450)


# submit
import inspect
import os

def write_agent_to_file(function, file):
    with open(file, "a" if os.path.exists(file) else "w") as f:
        f.write(inspect.getsource(function))
        print(function, "written to", file)

write_agent_to_file(my_agent, "submission.py")

# Check that submission file was created
# q_5.check()





















