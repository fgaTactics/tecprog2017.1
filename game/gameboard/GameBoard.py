# -- This class is responsable for draw the board at the screen -- #

import pygame
from gameEngine.GameObject import *
from game.gameboard.Square import *
from game.pieces.FreshMan import *

# RGB color definitions
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)


class GameBoard:
    # PARÂMETROS DE ENTRADA MUDAM (receber o número de colunas e linhas?)

    # Grid with all positions of squares at the board
    grid = []

    # Spacing in pixels between the board and the edges of the screen
    lateral_spacing = 217
    top_spacing = 180

    # Amount of rows and columns of the board
    amount_of_rows = 5
    amount_of_columns = 10

    # Positions in pixels of ending of the board
    end_position = (982, 555)

    # Square size of the board and margin size between them
    square_size = 60
    square_margin = 15

    def __init__(self, game_board_square_size=0):
        self.board_width = game_board_square_size
        self.board_height = game_board_square_size

        # Add all square positions
        for row in range(self.amount_of_rows):
            self.grid.append([])
            for column in range(self.amount_of_columns):
                square_positions = self.position_calculation(row, column)
                self.grid[row].append(Square(square_positions[0], square_positions[1]))
    # mover uma peça

    def position_calculation(self, row, column):
        square_positions = []
        x_position = (self.lateral_spacing + (self.square_margin + self.board_width) *
                      column + self.square_margin)
        y_position = (self.top_spacing + (self.square_margin + self.board_height) *
                      row + self.square_margin)

        square_positions.append(x_position)
        square_positions.append(y_position)

        return square_positions

    def draw(self, screen):
        # Draw all the squares that form the board
        for row in range(self.amount_of_rows):
            for column in range(self.amount_of_columns):
                self.grid[row][column].draw(screen, self.board_width, self.board_height)
