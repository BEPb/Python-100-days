"""
Python 3.9
Рекурсивный метод обратного отслеживания: называется эвристическим методом, поиск вперед в соответствии с оптимальными условиями, когда поиск достигает определенного шага,
Когда выясняется, что первоначальный выбор плох или цель не достигнута, он отступает и выбирает снова.
Классическая задача: рыцарский патруль
Название файла 'example05.py'

Version: 0.1
Author: Andrej Marinchenko
Date: 2021-11-18
"""
import os
import sys
import time

SIZE = 5
total = 0


def print_board(board):
    # os.system('clear')
    for row in board:
        for col in row:
            print(str(col).center(4), end='')
        print()


def patrol(board, row, col, step=1):
    if row >= 0 and row < SIZE and \
        col >= 0 and col < SIZE and \
        board[row][col] == 0:
        board[row][col] = step
        if step == SIZE * SIZE:
            global total
            total += 1
            print(f'{total}способ передвижения: ')
            print_board(board)
        patrol(board, row - 2, col - 1, step + 1)
        patrol(board, row - 1, col - 2, step + 1)
        patrol(board, row + 1, col - 2, step + 1)
        patrol(board, row + 2, col - 1, step + 1)
        patrol(board, row + 2, col + 1, step + 1)
        patrol(board, row + 1, col + 2, step + 1)
        patrol(board, row - 1, col + 2, step + 1)
        patrol(board, row - 2, col + 1, step + 1)
        board[row][col] = 0


def main():
    board = [[0] * SIZE for _ in range(SIZE)]
    patrol(board, SIZE - 1, SIZE - 1)


if __name__ == '__main__':
    main()
