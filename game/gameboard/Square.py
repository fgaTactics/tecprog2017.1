import pygame

CENTERING_CORRECTION = 5
# This class describes the board squares behavior.


class Square:
    def __init__(self, x_position, y_position, game_board_square_side,
                 square_color, x_board_position, y_board_position):

        self.width = game_board_square_side
        self.height = game_board_square_side
        self.initial_x_position = x_position
        self.initial_y_position = y_position
        self.color = square_color
        self.piece = None
        self.set_x(x_position)
        self.set_y(y_position)
        self.x_board_position = x_board_position
        self.y_board_position = y_board_position

    def has_piece(self):
        return True if self.piece is not None else False

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
                                              self.width, self.height])

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

    def get_x_board_position(self):
        return self.x_board_position

    def get_y_board_position(self):
        return self.y_board_position
