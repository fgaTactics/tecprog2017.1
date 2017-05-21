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
SQUARE_SIDE = 60
BOARD_LEFT_LIMIT = 240
BOARD_TOP_LIMIT = 200

class MovePieceScene(Scene):

    def __init__(self, name="DEFAULT", ID=0):
        logging.info("Constructing Move Piece Scene")

        super().__init__(name, ID)

        self.game_board = GameBoard(SQUARE_SIDE)

        # Space between board spaces
        self.board_start_x = self.game_board.lateral_spacing
        self.board_start_y = self.game_board.top_spacing

        # Board left and bottom limits, respectively
        self.board_end_x = self.game_board.end_position[0]
        self.board_end_y = self.game_board.end_position[1]

        # Traveled space in a piece "step" (single space moviment)
        self.piece_step_size = self.game_board.square_margin + self.game_board.square_size

        self.piece = FreshMan(HEALTH, ATTACK, RANGE_ATTACK, DEFENSE,
                              AMOUNT_OF_MOVIMENT, PENALTY, HABILITY,
                              DESCRIPTION, self.game_board.board[2][4].initial_x_position, self.game_board.board[2][4].initial_y_position, WIDTH,
                              HEIGHT, FILENAME)

        logging.info("Move Piece Scene is ready")


    # Define piece movements
    def update(self, event):
        logging.debug("Beginning Move Piece scene's update method")

        mouse = Mouse()

        if (mouse.is_mouse_click(self.piece, event)):
            logging.debug("Starting piece movement")
            
        else:
            pass

        logging.debug("Finishing Move Piece scene's update method")


    def get_clicked_square(self, event):
        for row in range(self.game_board.amount_of_rows):
            for column in range(self.game_board.amount_of_columns):
                square = self.game_board.board[row][column]
                rectangle = pygame.Rect(square.initial_x_position, 
                                        square.initial_y_position,
                                        square.side,
                                        square.side)
                
                if(event.type == pygame.MOUSEBUTTONUP):
                    mouse_position = pygame.mouse.get_pos()

                    if(rectangle.collidepoint(mouse_position[0], mouse_position[1])):
                        return (row, column)

    # Display piece in the correct position after movement
    def draw(self, screen, groups):
        logging.debug("Beginning Move Piece scene's draw method")

        self.game_board.draw(screen)
        self.piece.draw(screen, groups)

        logging.debug("Finishing Move Piece scene's draw method")
