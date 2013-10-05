import pygame
import random

from GameBoard import *
from Block import *


def main():
    pygame.init()

    height = 620
    width = height / 16 * 9

    screen = pygame.display.set_mode((width, height))
    font = pygame.font.Font(pygame.font.get_default_font(), 30)

    running = True
    elapsed_time = 0

    clock = pygame.time.Clock()

    current_block = Block(0, 5, 10)
    board = GameBoard(width, height)

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                break
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_DOWN:
                    current_block.y_pos += 1
                if event.key == pygame.K_LEFT:
                    if current_block.x_pos > 0:
                        current_block.x_pos -= 1
                if event.key == pygame.K_RIGHT:
                    if current_block.x_pos + current_block.block_width < board.grid_width:
                        current_block.x_pos += 1
                if event.key == pygame.K_UP:
                    current_block.rotate()

        if current_block.finished:
            board.add_block(current_block)
            current_block = Block(random.randint(0, 3), 0, 0)

        dt = clock.tick()
        elapsed_time += dt
        if elapsed_time > 500:
            elapsed_time = 0
            if current_block.frozen:
                current_block.finished = True
            current_block.y_pos += 1

        board.check_if_scored()
        board.update_board()
        board.update_block(current_block)
        board.render()

        screen.blit(board.display, (0, 0))
        screen.blit(font.render(str(board.score), True, (255, 255, 255)), (280, 30))
        pygame.display.flip()


main()