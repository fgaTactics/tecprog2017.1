# -- This class is responsable for draw the board at the screen -- #

import pygame
import logging
from gameEngine.GameObject import *
from gameEngine.Scene import *
from game.gameboard.Square import *
from game.pieces.FreshMan import *

# All the following constants are in pixel units
MININUM_SQUARE_SIZE = 0

# RGB color definitions
WHITE = (255, 255, 255)
GREY = (150, 150, 150)
GREEN = (0, 255, 0)
RED = (255, 0, 0)


class GameBoard:
    # Grid with all positions of squares at the board
    board = []

    # Spacing in pixels between the board and the edges of the screen
    lateral_spacing = 217
    top_spacing = 180

    # Amount of rows and columns of the board
    amount_of_rows = 5
    amount_of_columns = 10

    # Positions in pixels of ending of the board
    end_position = (982, 555)

    # Square margin size
    square_size = 60
    square_margin = 15

    def __init__(self, game_board_square_side=0):
        logging.info("Constructing GameBoard")

        assert game_board_square_side > MININUM_SQUARE_SIZE, "The size is invalid"

        self.game_board_square_side = game_board_square_side

        # Add all squares in the board
        for row in range(self.amount_of_rows):
            self.board.append([])
            for column in range(self.amount_of_columns):
                square_positions = self.position_calculation(row, column)
                square_color = WHITE
                self.board[row].append(Square(square_positions[0], square_positions[1],
                                              self.game_board_square_side, square_color))
        logging.info("The game board is ready")

    def position_calculation(self, row, column):
        logging.info("Beginnig position_calculation method")

        square_positions = []

        # Calculate the vertical and horizontal position of a square
        x_position = (self.lateral_spacing + (self.square_margin +
                                              self.game_board_square_side) *
                      column + self.square_margin)
        y_position = (self.top_spacing + (self.square_margin +
                                          self.game_board_square_side) *
                      row + self.square_margin)

        # Add the positions to an array
        square_positions.append(x_position)
        square_positions.append(y_position)

        logging.info("Exiting position_calculation method")

        return square_positions

    def draw(self, screen):
        logging.info("Beginnig GameBoard's draw method")
        assert screen is not None, "The screen can't be null"

        # Draw all the squares of the board
        for row in range(self.amount_of_rows):
            for column in range(self.amount_of_columns):
                self.board[row][column].draw(screen)

        logging.info("Exiting GameBoard's draw method")
