from gameEngine.Scene import *
from game.gameboard.GameBoard import *
from game.pieces.FreshMan import *
from gameEngine.Mouse import *

# Piece attributes values
# Numeric values in generic units
HEALTH = 0
ATTACK = 0
RANGE_ATTACK = 0
DEFENSE = 0
AMOUNT_OF_MOVIMENT = 1
PENALTY = 0
HABILITY = ""
DESCRIPTION = ""
FILENAME = "pieces/baja_pilot.png"
# Piece size in pixel units
WIDTH = 50
HEIGHT = 50

# Board attributes in pixel units
BOARD_WIDTH = 60
BOARD_HEIGHT = 60
BOARD_LEFT_LIMIT = 240
BOARD_TOP_LIMIT = 200


class MovePieceScene(Scene):

    def __init__(self, name="DEFAULT", ID=0):
        super().__init__(name, ID)

        self.game_board = GameBoard(BOARD_WIDTH, BOARD_HEIGHT)

        self.board_start_x = self.game_board.lateral_spacing
        self.board_start_y = self.game_board.top_spacing

        self.board_end_x = self.game_board.end_position[0]
        self.board_end_y = self.game_board.end_position[1]

        self.piece_step_size = self.game_board.square_margin + self.game_board.square_size

        self.piece = FreshMan(BOARD_LEFT_LIMIT, BOARD_TOP_LIMIT,
                              HEALTH, ATTACK, RANGE_ATTACK, DEFENSE,
                              AMOUNT_OF_MOVIMENT, PENALTY, HABILITY,
                              DESCRIPTION, WIDTH, HEIGHT, FILENAME)


    def update(self, event):
        mouse = Mouse()

        if (mouse.is_mouse_click(self.piece, event)):
            y = self.down_movement(self.piece.get_y())
            self.piece.set_y(y)
        else:
            pass


    def right_movement(self, current_x):
        if(current_x < (self.board_end_x - self.piece_step_size)):
            new_x_position = (current_x + self.piece_step_size)
            return new_x_position
        else:
            return current_x


    def left_movement(self, current_x):
        if(current_x > (self.board_start_x + self.piece_step_size)):
            new_x_position = (current_x - self.piece_step_size)
            return new_x_position
        else:
            return current_x


    def up_movement(self, current_y):
        if(current_y > (self.board_start_y + self.piece_step_size)):
            new_y_position = (current_y - self.piece_step_size)
            return new_y_position
        else:
            return current_y


    def down_movement(self, current_y):
        if(current_y < (self.board_end_y - self.piece_step_size)):
            new_y_position = (current_y + self.piece_step_size)
            return new_y_position
        else:
            return current_y


    def draw(self, screen, groups):
        self.game_board.draw(screen)
        self.piece.draw(screen, groups)
