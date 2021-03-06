"""
Python 3.9 программа тренировки текущей нейронной сети
программа на Python по изучению обучения с подкреплением - Reinforcement Learning
Название файла alphazero_agent.py

Version: 0.1
Author: Andrej Marinchenko
Date: 2021-12-23
"""
import os
import numpy as np
import parl
import torch
import torch.optim as optim

from tqdm import tqdm
from utils import *
from connect4_model import Connect4Model

args = dotdict({
    'lr': 0.001,
    'dropout': 0.3,
    'epochs': 25,  # 25 - 5 количество эпох для тренировки нейронной сети
    'batch_size': 64,  # указываем по сколько примеров обрабатывает наша нейронная сеть для обучения
    'num_channels': 64,
})


class AlphaZero(parl.Algorithm):
    def __init__(self, model):
        self.model = model

    def learn(self, boards, target_pis, target_vs, optimizer):
        self.model.train()  # режим тренировки   - train mode

        # compute model output
        # вычислить выходные данные модели
        out_log_pi, out_v = self.model(boards)

        pi_loss = -torch.sum(target_pis * out_log_pi) / target_pis.size()[0]

        v_loss = torch.sum(
            (target_vs - out_v.view(-1))**2) / target_vs.size()[0]

        total_loss = pi_loss + v_loss

        # compute gradient and do SGD step
        # вычисляем градиент и делаем шаг SGD
        optimizer.zero_grad()
        total_loss.backward()
        optimizer.step()

        return total_loss, pi_loss, v_loss

    def predict(self, board):
        self.model.eval()  # режим эволюции - eval mode

        with torch.no_grad():
            log_pi, v = self.model(board)

        pi = torch.exp(log_pi)
        return pi, v


def create_agent(game, cuda=True):
    cuda = cuda and torch.cuda.is_available()

    model = Connect4Model(game, args)
    if cuda:
        model.cuda()

    algorithm = AlphaZero(model)

    alphazero_agent = AlphaZeroAgent(algorithm, game, cuda)
    return alphazero_agent


class AlphaZeroAgent(parl.Agent):
    def __init__(self, algorithm, game, cuda):
        super(AlphaZeroAgent, self).__init__(algorithm)
        self.cuda = cuda
        self.board_x, self.board_y = game.getBoardSize()
        self.action_size = game.getActionSize()

    def learn(self, examples):  # Args: examples: list of examples, each example is of form (board, pi, v)
        """
        Эта функция используется на 2-м шаге каждой итерации для тренировки модели
        Аргументы: примеры: список примеров, каждый пример имеет форму (доска, пи, v)
        """
        optimizer = optim.Adam(self.alg.model.parameters(), lr=args.lr)

        for epoch in range(args.epochs):
            # print('EPOCH ::: ' + str(epoch + 1))
            print('Эпоха обучения нейронной сети ::: ' + str(epoch + 1))

            batch_count = int(len(examples) / args.batch_size)

            """ 
            прогресс тренировки по эпохам наблюдаем путем загрузки примеров через бар tqdm
            """
            # pbar = tqdm(range(batch_count), desc='Training Net')
            pbar = tqdm(range(batch_count), desc='Тренировка сети')
            for _ in pbar:
                sample_ids = np.random.randint(
                    len(examples), size=args.batch_size)
                boards, pis, vs = list(zip(*[examples[i] for i in sample_ids]))
                boards = torch.FloatTensor(np.array(boards).astype(np.float64))
                target_pis = torch.FloatTensor(np.array(pis))
                target_vs = torch.FloatTensor(np.array(vs).astype(np.float64))

                if self.cuda:
                    boards, target_pis, target_vs = boards.contiguous().cuda(
                    ), target_pis.contiguous().cuda(), target_vs.contiguous(
                    ).cuda()

                total_loss, pi_loss, v_loss = self.alg.learn(
                    boards, target_pis, target_vs, optimizer)

                # record loss with tqdm
                pbar.set_postfix(Loss_pi=pi_loss.item(), Loss_v=v_loss.item())

    def predict(self, board):
        # Args:
        #             board (np.array): input board
        #         Return:
        #             pi (np.array): probability of actions
        #             v (np.array): estimated value of input
        """
        Аргументы:
             board (np.array): плата ввода
         Возвращение:
             pi (np.array): вероятность действий
             v (np.array): оценочное значение ввода
        """
        # подготовка ввода - preparing input
        board = torch.FloatTensor(board.astype(np.float64))
        if self.cuda:
            board = board.contiguous().cuda()
        board = board.view(1, self.board_x, self.board_y)

        pi, v = self.alg.predict(board)

        return pi.data.cpu().numpy()[0], v.data.cpu().numpy()[0]

def create_agent(game, cuda=True):
    cuda = cuda and torch.cuda.is_available()

    model = Connect4Model(game, args)
    if cuda:
        model.cuda()

    algorithm = AlphaZero(model)

    alphazero_agent = AlphaZeroAgent(algorithm, game, cuda)
    return alphazero_agent
