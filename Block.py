__author__ = 'Andrew'


class Block():
    tetromino = 0

    color = (0, 0, 0)

    x_pos = 0
    y_pos = 0

    finished = False
    frozen = False

    tetrominos = [
        [['g', 'g', 'g', 'g']],

        [['r', 'r'],
         ['r', 'r']],

        [['b', 'b', 'b'],
         [0, 'b',  0]],

        [['o', 0],
         ['o', 'o'],
         [0, 'o']],

        [['p', 0],
         ['p', 0],
         ['p', 'p']]]

    def __init__(self, tetromino, x, y):
        self.tetromino = tetromino
        self.shape = self.tetrominos[tetromino]
        self.block_width = len(self.shape[0])
        self.block_height = len(self.shape)
        self.x_pos = x
        self.y_pos = y
        self.finished = False

    def rotate(self):
        self.shape = zip(*self.shape[::-1])
        self.block_width = len(self.shape[0])
        self.block_height = len(self.shape)



    def update(self, board):
        pass




