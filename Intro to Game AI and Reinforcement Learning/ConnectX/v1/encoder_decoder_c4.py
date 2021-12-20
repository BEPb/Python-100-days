"""
Python 3.9 список функций
Название файла encoder_decoder_c4.py

список функций для кодирования / декодирования класса платы Connect4 для ввода / интерпретации в нейронную сеть

Version: 0.1
Author: Andrej Marinchenko
Date: 2021-12-20
"""
#!/usr/bin/env python

import numpy as np
from connect_board import board

def encode_board(board):
    board_state = board.current_board
    encoded = np.zeros([6,7,3]).astype(int)
    encoder_dict = {"O":0, "X":1}
    for row in range(6):
        for col in range(7):
            if board_state[row,col] != " ":
                encoded[row, col, encoder_dict[board_state[row,col]]] = 1
    if board.player == 1:
        encoded[:,:,2] = 1 # player to move
    return encoded

def decode_board(encoded):
    decoded = np.zeros([6,7]).astype(str)
    decoded[decoded == "0.0"] = " "
    decoder_dict = {0:"O", 1:"X"}
    for row in range(6):
        for col in range(7):
            for k in range(2):
                if encoded[row, col, k] == 1:
                    decoded[row, col] = decoder_dict[k]
    cboard = board()
    cboard.current_board = decoded
    cboard.player = encoded[0,0,2]
    return cboard