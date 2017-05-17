import logging
from gameEngine.GameObject import *
from game.gameboard.GameBoard import *
from gameEngine.GameEngine import SCREEN_WIDTH
import math

# Distance to pull the piece into a valid square
SNAP_DISTANCE = GameBoard.square_size / 2 + GameBoard.square_margin

# Distance to centralize the piece into square of the board in pixels
CENTER_OF_SQUARE = 20

# Position on scene of players in pixels
X_POSITION_PLAYER_ONE = 232
Y_POSITION_PLAYER_ONE = 337
X_POSITION_PLAYER_TWO = 802
Y_POSITION_PLAYER_TWO = 967

""" -- This class is used to make pieces draggable and put then on the write
       position -- """


class DraggablePiece(GameObject):

    drag_enabled = True
    # Initialize the piece position and make the draggable space on the board

    def __init__(self, x_position, y_position, width, height, filename, piece_name):
        logging.info("Construction of the draggable piece")
        self.isDrag = False
        self.mousePosition = [0, 0]
        self.corners = []

        self.initial_piece_position = [0, 0]
        self.board_position = [0, 0]

        # Valid drag area for both players
        self.player_one_drag_area = [X_POSITION_PLAYER_ONE, Y_POSITION_PLAYER_ONE]
        self.player_two_drag_area = [X_POSITION_PLAYER_TWO, Y_POSITION_PLAYER_TWO]

        # Define the board space
        for x in range(GameBoard.lateral_spacing, GameBoard.end_position[0],
                       GameBoard.square_size + GameBoard.square_margin):
            for y in range(GameBoard.top_spacing, GameBoard.end_position[1],
                           GameBoard.square_size + GameBoard.square_margin):

                self.corners.append((x, y))

        self.initial_piece_position[0] = x_position
        self.initial_piece_position[1] = y_position
        self.name = piece_name
        self.image = filename

        super().__init__(x_position, y_position, width, height, filename)
        logging.info("End of draggable piece creation")


    # Draw on the screen the piece
    def draw(self, screen, groups):
        logging.debug("Draw the draggable piece")
        groups.add(self.sprite)
        logging.debug("Drew the draggable piece")

    # Upadate the piece position on the screen
    def update(self, event):
        logging.debug("Update the draggable piece")
        if(DraggablePiece.drag_enabled or
           (self.get_x() != self.initial_piece_position[0]) and
           (self.get_y() != self.initial_piece_position[1])):
            self.drag(event)
            logging.debug("dragging the piece with the mouse")
        else:
            # Do Nothing
            pass
        logging.debug("Updated the draggable piece")


    # Enable or desable the draggable pieces from the list to the board
    @classmethod
    def set_drag_enable(cls, drag_status):
        logging.info("Enable or desable piece from the list to the board")
        cls.drag_enabled = drag_status
        logging.info("Enabled or desabled piece from the list to the board")


    # Verify if the piece is being draged on the screen and change the piece position
    def drag(self, event):
        logging.info("Make the piece draggable")
        if(event.type == pygame.MOUSEBUTTONDOWN):
            self.mouse_position = pygame.mouse.get_pos()
            if(self.sprite.rect.collidepoint(self.mouse_position[0],
                                             self.mouse_position[1])):
                self.isDrag = True
                logging.info("Drag of new pieces enable")
        elif(event.type == pygame.MOUSEBUTTONUP):
            self.isDrag = False
            logging.info("Drag of new pieces desable")

        if(self.isDrag):
            self.mouse_position = pygame.mouse.get_pos()
            # Get the x and y position on the center of the square
            self.set_x(self.mouse_position[0] - self.width / 2)
            self.set_y(self.mouse_position[1] - self.height / 2)
            logging.info("Get the x and y position on the center of the square")

        else:
            self.verify_drag()
            logging.info("Called the verify_drag method with sucess")
        logging.info("Maked the piece draggable")


    # Verify if the piece was released on a valid position
    def verify_drag(self):
        logging.info("Verify if the piece was released on a valid position")
        sprite_topleft = self.sprite.rect.topleft

        for self.board_position[0], self.board_position[1] in self.corners:
            hypotenuse = math.hypot(self.board_position[0] - sprite_topleft[0],
                                    self.board_position[1] - sprite_topleft[1])

            if(self.initial_piece_position[0] < SCREEN_WIDTH / 2):
                if((self.player_one_drag_area[0] <= sprite_topleft[0] <=
                    self.player_one_drag_area[1]) and
                   (GameBoard.top_spacing <= sprite_topleft[1] <=
                    GameBoard.end_position[1]) and
                   (hypotenuse <= SNAP_DISTANCE)):

                    self.set_x(self.board_position[0] + CENTER_OF_SQUARE)
                    self.set_y(self.board_position[1] + CENTER_OF_SQUARE)
                    logging.info("Put the piece on the more close board square "
                                 "on the left side")
                    break
                else:
                    self.set_x(self.initial_piece_position[0])
                    self.set_y(self.initial_piece_position[1])
                    logging.info("Got the mouse position")
            else:
                if((self.player_two_drag_area[0] <= sprite_topleft[0] <=
                    self.player_two_drag_area[1]) and
                   (GameBoard.top_spacing <= sprite_topleft[1] <=
                    GameBoard.end_position[1]) and
                   (hypotenuse <= SNAP_DISTANCE)):

                    self.set_x(self.board_position[0] + CENTER_OF_SQUARE)
                    self.set_y(self.board_position[1] + CENTER_OF_SQUARE)
                    logging.info("Put the piece on the more close board square "
                                 "on the right side")
                    break
                else:
                    self.set_x(self.initial_piece_position[0])
                    self.set_y(self.initial_piece_position[1])
                    logging.info("Got the mouse position")
            logging.info("Verified if the piece was released on a valid position")
