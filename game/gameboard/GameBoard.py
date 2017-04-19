# -- This class is responsable for draw the board at the screen -- #

import pygame
from gameEngine.GameObject import *


# RGB color definitions
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)


class GameBoard:

    # Grid with all positions of squares at the board
    grid = []

    # Spacing between the board and the edges of the screen
    lateral_spacing = 217
    top_spacing = 180
    
    # Amount of rows and columns of the board
    amount_of_rows = 5
    amount_of_columns = 10

    # Size of squares of the board
    size_square = 60

    def __init__(self, board_width=0, board_height=0, square_margin=0):
        self.board_width = board_width
        self.board_height = board_height
        self.square_margin = square_margin

        # Add all square positions
        for row in range(self.amount_of_rows):
            self.grid.append([])
            for column in range(self.amount_of_columns):
                self.grid[row].append(0)


    def draw(self, screen):

        # Draw all the squares that form the board
        for row in range(self.amount_of_rows):
            for column in range(self.amount_of_columns):
                color = WHITE

                pygame.draw.rect(screen,
                                 color,
                                 [self.lateral_spacing +
                                  (self.square_margin + self.board_width) *
                                  column + self.square_margin,
                                  self.top_spacing +
                                  (self.square_margin + self.board_height) *
                                  row + self.square_margin,
                                  self.board_width,
                                  self.board_height])
