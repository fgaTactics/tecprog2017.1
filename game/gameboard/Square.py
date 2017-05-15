# All the following constants are pixels units
SQUARE_SIZE = 60

# This class describes the board squares behavior.


class Square:
    def __init__(self, x_position, y_position):
        self.x_position = x_position
        self.y_position = y_position
        self.side = SQUARE_SIZE
        self.has_piece = False
