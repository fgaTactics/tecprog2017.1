import pygame

CENTERING_CORRECTION = 5
# This class describes the board squares behavior.


class Square:
    def __init__(self, x_position, y_position, game_board_square_side, square_color):
        self.side = game_board_square_side
        self.initial_x_position = x_position
        self.initial_y_position = y_position
        self.color = square_color
        self.piece = None

    def has_piece(self):
        return True if self.piece is not None else False

    def get_piece(self):
        return self.piece

    def add_piece(self, piece):
        self.piece = piece
        piece.set_x(self.initial_x_position + CENTERING_CORRECTION)
        piece.set_y(self.initial_y_position + CENTERING_CORRECTION)

    def update_color(self, color):
        self.color = color

    def remove_piece(self):
        self.piece = None

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, [self.initial_x_position,
                                              self.initial_y_position,
                                              self.side, self.side])

    def update(self):
        pass
