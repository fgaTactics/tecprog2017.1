import logging
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
        logging.info("Constructing Move Piece Scene")

        super().__init__(name, ID)

        self.game_board = GameBoard(BOARD_WIDTH, BOARD_HEIGHT)

        # Space between board spaces
        self.board_start_x = self.game_board.lateral_spacing
        self.board_start_y = self.game_board.top_spacing

        # Board left and bottom limits, respectively
        self.board_end_x = self.game_board.end_position[0]
        self.board_end_y = self.game_board.end_position[1]

        # Traveled space in a piece "step" (single space moviment)
        self.piece_step_size = self.game_board.square_margin + self.game_board.square_size

        self.piece = FreshMan(BOARD_LEFT_LIMIT, BOARD_TOP_LIMIT,
                              HEALTH, ATTACK, RANGE_ATTACK, DEFENSE,
                              AMOUNT_OF_MOVIMENT, PENALTY, HABILITY,
                              DESCRIPTION, WIDTH, HEIGHT, FILENAME)

        logging.info("Move Piece Scene is ready")


    # Define piece movements
    def update(self, event):
        logging.debug("Beginning Move Piece scene's update method")

        mouse = Mouse()

        if (mouse.is_mouse_click(self.piece, event)):
            logging.debug("Starting piece movement")

            y = self.down_movement(self.piece.get_y())
            self.piece.set_y(y)
        else:
            pass

        logging.debug("Finishing Move Piece scene's update method")


    # One step piece movement to the right
    def right_movement(self, current_x):
        logging.debug("Start right movement")

        if(current_x < (self.board_end_x - self.piece_step_size)):
            logging.debug("Moving right")

            new_x_position = (current_x + self.piece_step_size)
            return new_x_position
        else:
            return current_x

        logging.debug("Finishing right movement")


    # One step piece movement to the left
    def left_movement(self, current_x):
        logging.debug("Start left movement")

        if(current_x > (self.board_start_x + self.piece_step_size)):
            logging.debug("Moving left")

            new_x_position = (current_x - self.piece_step_size)
            return new_x_position
        else:
            return current_x

        logging.debug("Finishing left movement")


    # One step up piece movement
    def up_movement(self, current_y):
        logging.debug("Start up movement")

        if(current_y > (self.board_start_y + self.piece_step_size)):
            logging.debug("Moving up")

            new_y_position = (current_y - self.piece_step_size)
            return new_y_position
        else:
            return current_y

        logging.debug("Finishing up movement")


    # One step down piece movement
    def down_movement(self, current_y):
        logging.debug("Start down movement")

        if(current_y < (self.board_end_y - self.piece_step_size)):
            logging.debug("Moving down")

            new_y_position = (current_y + self.piece_step_size)
            return new_y_position
        else:
            return current_y

        logging.debug("Finishing down movement")


    # Display piece in the correct position after movement
    def draw(self, screen, groups):
        logging.debug("Beginning Move Piece scene's draw method")

        self.game_board.draw(screen)
        self.piece.draw(screen, groups)

        logging.debug("Finishing Move Piece scene's draw method")
