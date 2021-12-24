"""
Python 3.9 программа 2 агента могут сражаться друг с другом (нужна для оценки прогресса развития модели)
программа на Python по изучению обучения с подкреплением - Reinforcement Learning
Название файла Arena.py

Version: 0.1
Author: Andrej Marinchenko
Date: 2021-12-23
"""
from tqdm import tqdm
from parl.utils import logger


class Arena():
    # An Arena class where any 2 agents can be pit against each other.
    """
    Класс арены, в котором любые 2 агента могут сражаться друг с другом.
    """

    def __init__(self, player1, player2, game, display=None):
        # Input:
        #             player 1,2: two functions that takes board as input, return action
        #             game: Game object
        #             display: a function that takes board as input and prints it (e.g.
        #                      display in othello/OthelloGame). Is necessary for verbose
        #                      mode.
        #
        #         see othello/OthelloPlayers.py for an example. See pit.py for pitting
        #         human players/other baselines with each other.
        """
        Вход:
             player 1,2: две функции, которые принимают доску в качестве входных данных, возвращают действие
             game: Игровой объект
             display: функция, которая принимает доску в качестве входных данных и печатает ее (например,
                      отображать в othello / OthelloGame). Необходимо для подробного
                      режим.

         см. пример othello / OthelloPlayers.py. См. Pit.py для получения информации о питтинге
         человеческие игроки / другие базовые уровни друг с другом.
        """
        self.player1 = player1
        self.player2 = player2
        self.game = game
        self.display = display

    def playGame(self, verbose=False):
        # Executes one episode of a game.
        #
        #         Returns:
        #             either
        #                 winner: player who won the game (1 if player1, -1 if player2)
        #             or
        #                 draw result returned from the game that is neither 1, -1, nor 0.
        """
        Выполняет один эпизод игры.
         Возврат:
             либо Победитель: игрок, выигравший игру (1, если player1, -1, если player2)
             или Результат draw, возвращенный из игры, не равен ни 1, ни -1, ни 0.
        """
        players = [self.player2, None, self.player1]
        curPlayer = 1
        board = self.game.getInitBoard()
        it = 0
        print('проверка развития модели на Арене')
        while self.game.getGameEnded(board, curPlayer) == 0:
            it += 1
            if verbose:
                assert self.display
                # print("Turn ", str(it), "Player ", str(curPlayer))
                print("Очередь ", str(it), "Игрок ", str(curPlayer))
                self.display(board)
            action = players[curPlayer + 1](self.game.getCanonicalForm(
                board, curPlayer))

            valids = self.game.getValidMoves(
                self.game.getCanonicalForm(board, curPlayer), 1)

            if valids[action] == 0:
                # logger.error('Action {} is not valid!'.format(action))
                logger.error('Действие {} недействительно!'.format(action))
                # logger.debug('valids = {}'.format(valids))
                logger.debug('действительно = {}'.format(valids))
                assert valids[action] > 0
            board, curPlayer = self.game.getNextState(board, curPlayer, action)
        if verbose:
            assert self.display
            # print("Game over: Turn ", str(it), "Result ", str(self.game.getGameEnded(board, 1)))
            print("Игра окончена: Очередь ", str(it), "Результат ", str(self.game.getGameEnded(board, 1)))
            self.display(board)
        return curPlayer * self.game.getGameEnded(board, curPlayer)

    def playGames(self, num, verbose=False):
        # Plays num games in which player1 starts num/2 games and player2 starts
        #         num/2 games.
        #         Returns:
        #             oneWon: games won by player1
        #             twoWon: games won by player2
        #             draws:  games won by nobody
        """
        Играет количество игр, в которых player1 начинает num / 2 игры, а player2 начинает
         кол-во / 2 игры.
         Возврат:
             oneWon: игры, выигранные игроком1
             twoWon: игры, выигранные player2
             ничьи: никем не выигранные партии
        """

        num = int(num / 2)
        oneWon = 0
        twoWon = 0
        draws = 0
        for _ in tqdm(range(num), desc="Arena.playGames (1)"):
            gameResult = self.playGame(verbose=verbose)
            if gameResult == 1:
                oneWon += 1
            elif gameResult == -1:
                twoWon += 1
            else:
                draws += 1

        self.player1, self.player2 = self.player2, self.player1

        for _ in tqdm(range(num), desc="Arena.playGames (2)"):
            gameResult = self.playGame(verbose=verbose)
            if gameResult == -1:
                oneWon += 1
            elif gameResult == 1:
                twoWon += 1
            else:
                draws += 1

        return oneWon, twoWon, draws
