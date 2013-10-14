__author__ = 'Andrew'
import pygame


class GameBoard():
    height = 0
    width = 0

    score = 0

    block_size = 20

    display = None

    grid = []
    blocks = []

    colors = {'r': (255, 0, 0),
              'g': (0, 255, 0),
              'b': (0, 0, 255),
              'o': (204, 102, 0),
              'p': (127, 0, 255),
              0: (0, 0, 0)}

    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.display = pygame.Surface((width, height))
        self.display.fill((0, 0, 255))
        self.init_arrays()
        self.grid_height = height/self.block_size
        self.grid_width = width/self.block_size

    def init_arrays(self):
        #generates two 2d arrays that hold the block data
        for y in range(self.height/self.block_size):
            self.grid.append([])
            for x in range(self.width/self.block_size):
                self.grid[y].append(0)
        for y in range(self.height/self.block_size):
            self.blocks.append([])
            for x in range(self.width/self.block_size):
                self.blocks[y].append(0)

    def render(self):
        #reads the data from grid array and then displays it
        for y in range(self.grid_height):
            for x in range(self.grid_width):
                block = pygame.Surface((self.block_size, self.block_size))
                block.fill(self.colors[self.grid[y][x]])
                self.display.blit(block, (x*self.block_size, y*self.block_size))

    def add_block(self, block):
        #reads shape data from the block object and copys it to blocks array at the blocks x and y position
        for y in range(block.block_height):
            for x in range(block.block_width):
                y_abs = y + block.y_pos
                x_abs = x + block.x_pos
                if block.shape[y][x] == 0:
                    continue
                if y_abs < self.grid_height:
                    self.blocks[y_abs][x_abs] = block.shape[y][x]

    def update_board(self):
        for y in range(len(self.blocks)):
            for x in range(len(self.blocks[0])):
                self.grid[y][x] = self.blocks[y][x]
        self.move_blocks_down()

    def update_block(self, block):
        for y in range(block.block_height):
            for x in range(block.block_width):
                y_abs = y + block.y_pos
                x_abs = x + block.x_pos

                #does not render zeroes in the block shape
                if block.shape[y][x] == 0:
                    continue
                if block.y_pos + block.block_height >= self.grid_height:
                    block.finished = True

                #collision detection
                if y_abs <= self.grid_height-2:
                        if not self.blocks[y_abs+1][x_abs] == 0:
                            block.finished = True

                self.grid[y_abs][x_abs] = block.shape[y][x]

    def check_if_scored(self):

        for y in xrange(self.grid_height):
            count = 0
            for x in xrange(self.grid_width):
                if self.blocks[y][x] != 0:
                    count += 1
            if count == self.grid_width:
                self.clear_row(y)
                self.score += 100

    def move_blocks_down(self):
        for y in xrange(self.grid_height - 1):
            for x in xrange(self.grid_width):
                if self.blocks[y][x] != 0 and self.blocks[y+1][x] == 0:
                    self.blocks[y+1][x] = self.blocks[y][x]
                    self.blocks[y][x] = 0

    def clear_row(self, row):
        for x in xrange(self.grid_width):
            self.blocks[row][x] = 0







