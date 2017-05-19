import pygame

WHITE = (255, 255, 255)
# This class describes the board squares behavior.


class Square:
    def __init__(self, x_position, y_position, game_board_square_side):
        self.x_position = x_position
        self.y_position = y_position
        self.side = game_board_square_side
        self.piece = None

    def has_piece(self):
        return True if self.piece is not None else False

    def add_piece(self, piece):
        self.piece = piece

    def remove_piece(self):
        self.piece = None

    def draw(self, screen):
        pygame.draw.rect(screen, WHITE, [self.x_position, self.y_position, self.side,
                                         self.side])

    def update(self):
        pass
