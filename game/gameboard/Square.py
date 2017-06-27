import pygame
from game.pieces.BasicPiece import *

CENTERING_CORRECTION = 5
# This class describes the board squares behavior.


class Square(GameObject):
    def __init__(self, x_position, y_position, board_square_size,
                 square_color, x_board_position, y_board_position):
        self.set_width(board_square_size)
        self.set_height(board_square_size)
        self.initial_x_position = x_position
        self.initial_y_position = y_position
        self.color = square_color
        self.piece = None
        self.set_x(x_position)
        self.set_y(y_position)
        self.x_board_position = x_board_position
        self.y_board_position = y_board_position

    def has_piece(self):
        if(self.piece is not None):
            return True
        else:
            return False

    def get_piece(self):
        return self.piece

    def add_piece(self, piece):
        self.piece = piece
        piece.set_square(self)
        piece.set_x(self.initial_x_position + CENTERING_CORRECTION)
        piece.set_y(self.initial_y_position + CENTERING_CORRECTION)

    def update_color(self, color):
        self.color = color

    def remove_piece(self):
        self.piece = None

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, [self.initial_x_position,
                                              self.initial_y_position,
                                              self.__width, self.__height])

    def update(self):
        pass

    def set_x(self, x_position):
        self.x_position = x_position

    def get_x(self):
        return self.x_position

    def set_y(self, y_position):
        self.y_position = y_position

    def get_y(self):
        return self.y_position

    def get_width(self):
        return self.__width

    def set_width(self, width):
        assert(width > 0), "Can't have an invisible square"
        self.__width = width

    def get_height(self):
        return self.__height

    def set_height(self, height):
        assert(height > 0), "Can't have an invisible square"
        self.__height = height

    def get_x_board_position(self):
        return self.x_board_position

    def get_y_board_position(self):
        return self.y_board_position
