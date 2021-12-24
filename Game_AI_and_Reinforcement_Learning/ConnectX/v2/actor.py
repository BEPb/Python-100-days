"""
Python 3.9 программа самостоятельной игры агентов текущего и предыдущего покаления
программа на Python по изучению обучения с подкреплением - Reinforcement Learning
Название файла actor.py

Version: 0.1
Author: Andrej Marinchenko
Date: 2021-12-23
"""
import numpy as np
import parl
import os
from alphazero_agent import create_agent
from MCTS import MCTS
from Arena import Arena
from utils import win_loss_draw


@parl.remote_class(wait=False)
class Actor(object):
    def __init__(self, game, args, seed):
        np.random.seed(seed)
        os.environ['OMP_NUM_THREADS'] = "1"
        self.game = game
        self.args = args

        # neural network of previous generation
        # нейронная сеть предыдущего поколения
        self.previous_agent = create_agent(self.game, cuda=False)
        # neural network of current generation
        # нейронная сеть текущего поколения
        self.current_agent = create_agent(self.game, cuda=False)

        # MCTS of previous generation
        # MCTS предыдущего поколения
        self.previous_mcts = MCTS(
            self.game, self.previous_agent, self.args, dirichlet_noise=True)
        # MCTS of current generation
        # MCTS текущего поколения
        self.current_mcts = MCTS(
            self.game, self.current_agent, self.args, dirichlet_noise=True)

    def self_play(self, current_weights, game_num):
        # Collecting training data by self-play.
        #         Args:
        #             current_weights (numpy.array): latest weights of neural network
        #             game_num (int): game number of self-play
        #         Returns:
        #             train_examples (list): examples of the form (canonicalBoard, currPlayer, pi,v)
        """
            Сбор данных о тренировках путем самостоятельной игры.
         Аргументы:
             current_weights (numpy.array): последние веса нейронной сети
             game_num (int): номер игры для самостоятельной игры
         Возврат:
             train_examples (список): примеры формы (canonicalBoard, currPlayer, pi, v)
        """

        print('Самостоятельная игра одного из созданных агентов (использует одно ядро)')
        # update weights of current neural network with latest weights
        # обновить веса текущей нейронной сети с последними весами
        self.current_agent.set_weights(current_weights)

        train_examples = []   # создаем пустую таблицу (список) тренировки
        for _ in range(game_num):
            # reset node state of MCTS
            print('сбросить состояние узла MCTS')
            self.current_mcts = MCTS(self.game, self.current_agent, self.args, dirichlet_noise=True)
            print('тренировка узла MCTS')
            train_examples.extend(self._executeEpisode())
        return train_examples

    def pitting(self, previous_weights, current_weights, games_num):
        # Fighting between previous generation agent and current generation agent
        #         Args:
        #             previous_weights (numpy.array): weights of previous generation neural network
        #             current_weights (numpy.array): weights of
        #         Returns:
        #             tuple of (game number of previous agent won, game number of current agent won, game number of draw)
        """Борьба между агентом предыдущего поколения и агентом текущего поколения
         Аргументы:
             previous_weights (numpy.array): веса нейронной сети предыдущего поколения
             current_weights (numpy.array): веса нейронной сети текущего поколения
             game_num (int): количество боев в игре
         Возврат:
             кортеж из (номер игры, в которой выиграл предыдущий агент, номер игры, в которой выиграл текущий агент,
             номер игры, в которой был проведен розыгрыш)
        """
        print('Борьба')
        # update weights of previous and current neural network
        # обновить веса предыдущей и текущей нейронной сети
        self.previous_agent.set_weights(previous_weights)
        self.current_agent.set_weights(current_weights)

        # reset node state of MCTS
        # сбросить состояние узла MCTS
        print('сбросить состояние узла MCTS перед ареной')
        self.previous_mcts = MCTS(self.game, self.previous_agent, self.args)
        self.current_mcts = MCTS(self.game, self.current_agent, self.args)

        arena = Arena(
            lambda x: np.argmax(self.previous_mcts.getActionProb(x, temp=0)),
            lambda x: np.argmax(self.current_mcts.getActionProb(x, temp=0)),
            self.game)
        previous_wins, current_wins, draws = arena.playGames(games_num)

        return (previous_wins, current_wins, draws)

    def evaluate_test_dataset(self, current_weights, test_dataset):
        # Evaluate performance of latest neural nerwork
        #         Args:
        #             current_weights (numpy.array): latest weights of neural network
        #             test_dataset (list): game number of self-play
        #         Returns:
        #             tuple of (number of perfect moves, number of good moves)
        """
        Оценить эффективность новейших нейронных сетей
         Аргументы:
             current_weights (numpy.array): последние веса нейронной сети
             test_dataset (список): номер игры для самостоятельной игры
         Возврат:
             кортеж из (количество совершенных ходов, количество хороших ходов)
        """
        print('Эволюция')
        # update weights of current neural network with latest weights
        # обновить веса текущей нейронной сети с последними весами
        self.current_agent.set_weights(current_weights)

        # определяем качество проведенной игры
        perfect_move_count, good_move_count = 0, 0
        for data in test_dataset:
            self.current_mcts = MCTS(self.game, self.current_agent, self.args)  # обращаемся к дереву MCTS

            x = self.game.getCanonicalForm(data['board'], data['player'])
            agent_move = int(np.argmax(self.current_mcts.getActionProb(x, temp=0)))  # количество ходов

            moves = data["move_score"]  # список очков
            perfect_score = max(moves)  # определяем максимальное значение в списке очков
            perfect_moves = [i for i in range(7) if moves[i] == perfect_score]  # выбираем 7 лучших

            if agent_move in perfect_moves:
                perfect_move_count += 1  # подсчет идеальных ходов
                print('perfect_move_count', perfect_move_count)

            print('Определяем победа\пройгрыш\ничья')
            if win_loss_draw(moves[agent_move]) == win_loss_draw(perfect_score):
                good_move_count += 1  # подсчет хороших ходов
                print('good_move_count', good_move_count)

        return (perfect_move_count, good_move_count)

    def _executeEpisode(self):
        # This function executes one episode of self-play, starting with player 1.
        #         As the game goes on, each turn is added as a training example to
        #         trainExamples. The game is played till the game ends. After the game
        #         ends, the outcome of the game is used to assign values to each example
        #         in trainExamples.
        #
        #         It uses a temp=1 if episodeStep < tempThresholdStep, and thereafter
        #         uses temp=0.
        #
        #         Returns:
        #             trainExamples: a list of examples of the form (canonicalBoard, currPlayer, pi,v)
        #                            pi is the MCTS informed policy vector, v is +1 if
        #                            the player eventually won the game, else -1.
        """
        Эта функция выполняет один эпизод самостоятельной игры, начиная с игрока 1.
         По ходу игры каждый ход добавляется в качестве обучающего примера к
         trainExamples. Игра длится до конца. После игры
         заканчивается, результат игры используется для присвоения значений каждому примеру
         в поезде Примеры.

         Он использует temp = 1, если episodeStep <tempThresholdStep, и после этого
         использует temp = 0.

         Возврат:
             trainExamples: список примеров формы (canonicalBoard, currPlayer, pi, v)
                            pi - вектор политики, проинформированный MCTS, v - +1, если
                            игрок в конце концов выиграл игру, иначе -1.
        """
        print('Эпизод одной игры')
        trainExamples = []
        board = self.game.getInitBoard()
        self.curPlayer = 1
        episodeStep = 0

        while True:
            episodeStep += 1
            print('Самостоятельная игра агентов текущего поколения и предыдущего, ход = ', episodeStep)
            canonicalBoard = self.game.getCanonicalForm(board, self.curPlayer)
            temp = int(episodeStep < self.args.tempThresholdStep)

            pi = self.current_mcts.getActionProb(canonicalBoard, temp=temp)
            sym = self.game.getSymmetries(canonicalBoard, pi)
            for b, p in sym:  # board, pi
                trainExamples.append([b, self.curPlayer, p, None])

            action = np.random.choice(len(pi), p=pi)
            board, self.curPlayer = self.game.getNextState(
                board, self.curPlayer, action)

            r = self.game.getGameEnded(board, self.curPlayer)

            if r != 0:
                return [(x[0], x[2], r * ((-1)**(x[1] != self.curPlayer)))
                        for x in trainExamples]
