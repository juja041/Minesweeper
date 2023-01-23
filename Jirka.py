import pygame

class Game():
    def __init__(self, board, size):
        self.board = board
        self.size = size

    def run(self):
        pygame.init()
        screen =  pygame.display.set_mode(size)
        