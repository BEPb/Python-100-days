import numpy as np  # базовые методы для манипуляции с большими массивами и матрицами
from collections import namedtuple  # реализует специализированные типы данных контейнеров

DEFAULT_HEIGHT = 6  # ширина рабочего стола игры
DEFAULT_WIDTH = 7  # высота рабочего стола игры
DEFAULT_WIN_LENGTH = 4  # выйгр. длинна???

WinState = namedtuple('WinState', 'is_ended winner')  # создаем контейнер из двух колонок 'статистика побед' и 'закончился победитель'


class Board():  # создаем класс доски (рабочего поля игры)
    """
    Connect4 Board.
    создаем класс доски (рабочего поля игры)
    """

    def __init__(self,  # функция инициализации на входе:
                 height=None,  # ширина
                 width=None,  # высота
                 win_length=None,  # выйгр. длинна
                 np_pieces=None):  # нп части
        # "Set up initial board configuration."
        "Настройте начальную конфигурацию доски."
        self.height = height or DEFAULT_HEIGHT  # ширина доски по умолчанию
        self.width = width or DEFAULT_WIDTH  # высота додски по умолчанию
        self.win_length = win_length or DEFAULT_WIN_LENGTH  # выйгр. длинна по умолчанию

        if np_pieces is None:  # если не заданы нп. части
            self.np_pieces = np.zeros([self.height, self.width], dtype=np.int)  # создаем пустую таблицу размерности
            # игральной доски
        else:
            self.np_pieces = np_pieces
            assert self.np_pieces.shape == (self.height, self.width)  # определяем представление формы и размера массива

    def add_stone(self, column, player):  # функция добавления камня
        #"Create copy of board containing new stone."
        "Создайте копию доски, содержащую новый камень."
        available_idx, = np.where(self.np_pieces[:, column] == 0)  # Возвращает элементы, выбранные из таблицы в
        # которых elf.np_pieces[:, column] = 0
        if len(available_idx) == 0:
            raise ValueError(
                # "Can't play column %s on board %s" % (column, self))
                "Невозможно воспроизвести столбец %s на доске %s" % (column, self))

        self.np_pieces[available_idx[-1]][column] = player

    def get_valid_moves(self):
        #"Any zero value in top row in a valid move"
        "Любое нулевое значение в верхней строке допустимого хода"
        return self.np_pieces[0] == 0

    def get_win_state(self):  # функция проверки условия победы
        for player in [-1, 1]:  # проверяет условия сначала для одного игрока затем для второго
            player_pieces = self.np_pieces == -player
            # Check rows & columns for win
            "Проверяйте строки и столбцы на победу"
            if (self._is_straight_winner(player_pieces)  # проверка выйгрыша по горизонтали
                    or self._is_straight_winner(player_pieces.transpose())  # проверка выйгрыша по вертикали
                    or self._is_diagonal_winner(player_pieces)):  # проверка выйгрыша по диагонали
                return WinState(True, -player)  # если условие выйгрыша подтверждается возвращает WinState(истина и
                # номер игрока)

        # draw has very little value.
        "ничья имеет очень небольшую ценность."
        if not self.get_valid_moves().any():  # если вся нулевая (верхняя) строка заполнена - ничья
            return WinState(True, None)  # если условие ничьей подтверждается возвращает WinState(истина и никто)

        # Game is not ended yet.
        "иначе Игра еще не окончена."
        return WinState(False, None)

    def with_np_pieces(self, np_pieces):
        # """Create copy of board with specified pieces."""
        """Создать копию доски с указанными частями."""
        if np_pieces is None:
            np_pieces = self.np_pieces
        return Board(self.height, self.width, self.win_length, np_pieces)

    def _is_diagonal_winner(self, player_pieces):
        # """Checks if player_pieces contains a diagonal win."""
        """Проверяет, есть ли в player_pieces диагональный выигрыш."""
        win_length = self.win_length
        for i in range(len(player_pieces) - win_length + 1):
            for j in range(len(player_pieces[0]) - win_length + 1):
                if all(player_pieces[i + x][j + x] for x in range(win_length)):
                    return True
            for j in range(win_length - 1, len(player_pieces[0])):
                if all(player_pieces[i + x][j - x] for x in range(win_length)):
                    return True
        return False

    def _is_straight_winner(self, player_pieces):
        # """Checks if player_pieces contains a vertical or horizontal win."""
        """Проверяет, содержит ли player_pieces вертикальный или горизонтальный выигрыш."""
        run_lengths = [
            player_pieces[:, i:i + self.win_length].sum(axis=1)
            for i in range(len(player_pieces) - self.win_length + 2)
        ]
        return max([x.max() for x in run_lengths]) >= self.win_length

    def __str__(self):
        return str(self.np_pieces)


class Connect4Game(object):
    # Connect4 Game class implementing the alpha-zero-general Game interface. Use 1 for player1 and -1 for player2.
    """
    Connect4 Game - класс, реализующий общий интерфейс игры alpha-zero. Используйте 1 для player1 и -1 для player2.
    """

    def __init__(self,
                 height=None,
                 width=None,
                 win_length=None,
                 np_pieces=None):
        self._base_board = Board(height, width, win_length, np_pieces)

    def getInitBoard(self):
        # Returns: startBoard: a representation of the board (ideally this is the form that will be the input to your neural network)
        """
        Возвращает: startBoard: представление доски (в идеале это форма, которая будет входить в вашу нейронную сеть)
        """
        return self._base_board.np_pieces

    def getBoardSize(self):
        """
        Returns: (x,y): a tuple of board dimensions
        Возвращает: (x, y): набор размеров платы
        """
        return (self._base_board.height, self._base_board.width)

    def getActionSize(self):
        """
        Returns: actionSize: number of all possible actions
        Возвращает: actionSize: количество всех возможных действий
        """
        return self._base_board.width

    def getNextState(self, board, player, action):
        """Returns a copy of the board with updated move, original board is unmodified.

        Input:
            board: current board
            player: current player (1 or -1)
            action: action taken by current player

        Returns:
            nextBoard: board after applying action
            nextPlayer: player who plays in the next turn (should be -player)

            Возвращает копию доски с обновленным ходом, исходная доска не изменена.

         Вход:
             доска: текущая доска
             player: текущий игрок (1 или -1)
             действие: действие, выполненное текущим игроком

         Возврат:
             nextBoard: доска после применения действия
             nextPlayer: игрок, который играет в следующий ход (должен быть -player)

        """
        b = self._base_board.with_np_pieces(np_pieces=np.copy(board))
        b.add_stone(action, player)
        return b.np_pieces, -player

    def getValidMoves(self, board, player):
        """Any zero value in top row in a valid move.

        Input:
            board: current board
            player: current player

        Returns:
            validMoves: a binary vector of length self.getActionSize(), 1 for
                        moves that are valid from the current board and player,
                        0 for invalid moves

            Любое нулевое значение в верхней строке допустимого хода.

         Вход:
             доска: текущая доска
             player: текущий игрок

         Возврат:
             validMoves: двоичный вектор длины self.getActionSize (), 1 для
                         ходы, которые действительны для текущей доски и игрока,
                         0 за неверные ходы
        """
        return self._base_board.with_np_pieces(
            np_pieces=board).get_valid_moves()

    def getGameEnded(self, board, player):
        """
        Input:
            board: current board
            player: current player (1 or -1)

        Returns:
            r: 0 if game has not ended. 1 if player won, -1 if player lost,
               small non-zero value for draw.

            Вход:
             доска: текущая доска
             player: текущий игрок (1 или -1)

         Возврат:
             r: 0, если игра не закончилась. 1, если игрок выиграл, -1, если игрок проиграл,
                небольшое ненулевое значение для розыгрыша.
        """
        b = self._base_board.with_np_pieces(np_pieces=board)
        winstate = b.get_win_state()
        if winstate.is_ended:
            if winstate.winner is None:
                # draw has very little value.
                return 1e-4
            elif winstate.winner == player:
                return +1
            elif winstate.winner == -player:
                return -1
            else:
                # raise ValueError('Unexpected winstate found: ', winstate)
                raise ValueError('Обнаружено неожиданное состояние WinState: ', winstate)
        else:
            # 0 used to represent unfinished game.
            return 0

    def getCanonicalForm(self, board, player):
        """ 
        Input:
            board: current board
            player: current player (1 or -1)

        Returns:
            canonicalBoard: returns canonical form of board. The canonical form
                            should be independent of player. For e.g. in chess,
                            the canonical form can be chosen to be from the pov
                            of white. When the player is white, we can return
                            board as is. When the player is black, we can invert
                            the colors and return the board.
        Вход:
             доска: текущая доска
             player: текущий игрок (1 или -1)

         Возврат:
             canonicalBoard: возвращает каноническую форму доски. Каноническая форма
                             не должен зависеть от игрока. Например, в шахматы,
                             каноническая форма может быть выбрана из от первого лица
                             белого. Когда игрок белый, мы можем вернуться
                             доска как есть. Когда игрок черный, мы можем инвертировать
                             цвета и вернуть доску.
        """
        return board * player

    def getSymmetries(self, board, pi):
        """Board is left/right board symmetric

        Input:
            board: current board
            pi: policy vector of size self.getActionSize()

        Returns:
            symmForms: a list of [(board,pi)] where each tuple is a symmetrical
                       form of the board and the corresponding pi vector. This
                       is used when training the neural network from examples.

            Доска левая / правая, доска симметричная

         Вход:
             доска: текущая доска
             pi: вектор политики размера self.getActionSize ()

         Возврат:
             symmForms: список [(board, pi)], где каждый кортеж является симметричным
                        форма доски и соответствующий вектор пи. Этот
                        используется при обучении нейронной сети на примерах.
        """
        return [(board, pi),
                (np.array(board[:, ::-1], copy=True),
                 np.array(pi[::-1], copy=True))]

    def stringRepresentation(self, board):
        """
        Input:
            board: current board

        Returns:
            boardString: a quick conversion of board to a string format.
                         Required by MCTS for hashing.

        Вход:
             доска: текущая доска

         Возврат:
             boardString: быстрое преобразование платы в строковый формат.
                          Требуется MCTS для хеширования.
        """
        return board.tostring()

    @staticmethod
    def display(board):
        print(" -----------------------")
        print(' '.join(map(str, range(len(board[0])))))
        print(board)
        print(" -----------------------")
