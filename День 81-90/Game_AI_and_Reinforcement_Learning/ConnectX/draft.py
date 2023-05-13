class board():
    def __init__(self):
        self.init_board = np.zeros([6,7]).astype(str)
        self.init_board[self.init_board == "0.0"] = " "
        self.player = 0
        self.current_board = self.init_board

