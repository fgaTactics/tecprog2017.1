# -- This class is responsable for draw the board at the screen -- #
import math
import pygame
import logging
from gameEngine.GameObject import *
from gameEngine.Scene import *
from game.gameboard.Square import *
from game.pieces.FreshMan import *
from gameEngine.Exceptions.SquareNotFoundError import *

# All the following constants are in pixel units
# Square margin size

# RGB color definitions
WHITE = (255, 255, 255)
GREY = (150, 150, 150)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

MINIMUM_SQUARE_SIZE = 40
MAXIMUM_SQUARE_SIZE = 60

MINIMUM_AMOUNT_OF_COLUMNS = 1
MAXIMUM_AMOUNT_OF_COLUMNS = 10
MINIMUM_AMOUNT_OF_ROWS = 1
MAXIMUM_AMOUNT_OF_ROWS = 5


class GameBoard:
    # Grid with all positions of squares at the board
    board = []

    square_size = 60
    square_margin = 15

    # Distance to pull the piece into a valid square
    SNAP_DISTANCE = square_size / 2 + square_margin

    # Spacing in pixels between the board and the edges of the screen
    lateral_spacing = 217
    top_spacing = 180

    # Amount of rows and columns of the board
    amount_of_rows = 5
    amount_of_columns = 10

    # Positions in pixels of ending of the board
    end_position = (982, 555)


    instance = None

    def __init__(self, game_board_square_side=0):
        logging.info("Constructing GameBoard")
        assert game_board_square_side > 0, "Can't have an invisible square"

        GameBoard.instance = self

        self.game_board_square_side = game_board_square_side

        # Add all squares in the board
        for row in range(self.amount_of_rows):
            self.board.append([])
            for column in range(self.amount_of_columns):
                square_positions = self.position_calculation(row, column)
                square_color = WHITE
                self.board[row].append(Square(square_positions[0], square_positions[1],
                                              self.game_board_square_side, square_color,
                                              row, column))

        logging.info("The game board is ready")

    def position_calculation(self, row, column):
        logging.info("Calculating square position")

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

    def get_closest_square(self, draggable_piece):
        x_position = draggable_piece.get_x()
        y_position = draggable_piece.get_y()
        smaller_hypotenuse = None
        closest_square = None
        for i in range(0, self.amount_of_rows):
            for j in range(0, self.amount_of_columns):
                # The distance between the square and the board is the hypotenuse
                hypotenuse = math.hypot(self.board[i][j].get_x() - x_position,
                                        self.board[i][j].get_y() - y_position)

                if(smaller_hypotenuse is None or smaller_hypotenuse > hypotenuse):
                    # The Smaller hypotenuse is the closest square to the piece
                    smaller_hypotenuse = hypotenuse
                    closest_square = self.board[i][j]
                else:
                    # Do nothing
                    pass


        if(self.__verify_valid_position(draggable_piece, closest_square,
                                        smaller_hypotenuse)):
            return closest_square
        else:
            raise SquareNotFoundError()


    # Verify if the piece was released on a valid column of the board
    def __verify_valid_position(self, draggable_piece, closest_square, hypotenuse):
        assert(hypotenuse >= 0), "The hypotenuse must be greater or equal to 0"

        if((not closest_square.has_piece()) and
           # The Closest square must be inside the player drag area X
           (draggable_piece.player_drag_area[0] <= closest_square.get_x() <=
            draggable_piece.player_drag_area[1]) and
           # The Closest square must be inside the player drag area Y
           (GameBoard.top_spacing <= closest_square.get_y() <=
            GameBoard.end_position[1]) and
           # The player can drag a piece outside the board, distance needs to be checked
           (hypotenuse <= self.SNAP_DISTANCE)):
            return True
        else:
            return False


    def draw(self, screen):
        logging.info("Beginnig GameBoard's draw method")
        assert screen is not None, "The screen can't be null"

        # Draw all the squares of the board
        for row in range(self.amount_of_rows):
            for column in range(self.amount_of_columns):
                self.board[row][column].draw(screen)

        logging.info("Exiting GameBoard's draw method")

    @classmethod
    def get_instance(cls):
        return cls.instance

    def get_board(self):
        assert(self.board is not None)
        return self.board

    def get_board_square_size(self):
        assert(self.square_size is not None)
        return self.square_size

    def get_amount_of_rows(self):
        assert(self.amount_of_rows is not None)
        return self.amount_of_rows

    def get_amount_of_columns(self):
        assert(self.amount_of_columns is not None)
        return self.amount_of_columns

    def set_board_square_size(self, square_size):
        assert isinstance(square_size, int), 'Square size must be an integer!'
        assert(amount_of_columns >= MINIMUM_SQUARE_SIZE and
                   amount_of_columns <= MAXIMUM_SQUARE_SIZE,
                   "Board square size must be between 40 and 60 units")

        self.square_size = square_size

    def set_amount_of_rows(self, amount_of_rows):
        assert isinstance(amount_of_rows, int), 'Amount of rows must be an integer!'
        assert(amount_of_columns >= MINIMUM_AMOUNT_OF_ROWS and
               amount_of_columns <= MAXIMUM_AMOUNT_OF_ROWS,
               "Amount of rows must be between 1 and 5")

        self.amount_of_rows = amount_of_rows

    def set_amount_of_columns(self, amount_of_columns):
        assert isinstance(amount_of_columns, int), 'Amount of columns must be an integer!'
        assert(amount_of_columns >= MINIMUM_AMOUNT_OF_COLUMNS and
               amount_of_columns <= MAXIMUM_AMOUNT_OF_COLUMNS,
               "Amount of columns must be between 1 and 10")

        self.amount_of_columns = amount_of_columns
