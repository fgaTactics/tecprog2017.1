# All the following constants are pixels units
SQUARE_SIZE = 60

# This class describes the board squares behavior.


class Square:
    def __init__(self, x_position, y_position):
        self.x_position = x_position
        self.y_position = y_position
        self.side = SQUARE_SIZE
        self.piece = None

    def has_piece(self):
        return True if self.piece is not None else False

    def add_piece(self, piece):
        self.piece = piece

    def remove_piece(self):
        self.piece = None

    def draw(self, screen, groups):
        pass

    def update(self):
        pass
