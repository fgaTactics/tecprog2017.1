import logging
from gameEngine.GameObject import *
from game.gameboard.GameBoard import *
from gameEngine.GameEngine import SCREEN_WIDTH
import math

# Distance to pull the piece into a valid square
SNAP_DISTANCE = GameBoard.square_size / 2 + GameBoard.square_margin

# Distance to centralize the piece into square of the board in pixels
CENTER_OF_SQUARE = 20

# Begin and End of army space of each player in pixels
PLAYER_ONE_BEGIN_INTERVAL = 232
PLAYER_ONE_END_INTERVAL = 337
PLAYER_TWO_BEGIN_INTERVAL = 802
PLAYER_TWO_END_INTERVAL = 937


""" -- This class is used to make pieces draggable and put then on a valid
       position in the game board -- """


class DraggablePiece(GameObject):

    drag_enabled = True


    """ Initialize the initial piece position and define the draggable space
        on the board """
    def __init__(self, x_position, y_position, width, height, filename, piece_name):
        logging.info("Building draggable piece")
        self.isDrag = False
        self.mousePosition = [0, 0]
        self.corners = []

        self.initial_board_position = [0, 0]

        # Define the board space to pull pieces into squares of the board
        for x in range(GameBoard.lateral_spacing, GameBoard.end_position[0],
                       GameBoard.square_size + GameBoard.square_margin):
            for y in range(GameBoard.top_spacing, GameBoard.end_position[1],
                           GameBoard.square_size + GameBoard.square_margin):

                self.corners.append((x, y))

        # Catching some informations of the piece
        self.initial_board_position[0] = x_position
        self.initial_board_position[1] = y_position
        self.name = piece_name
        self.image = filename

        # Set valid drag area for both players
        if(self.initial_board_position[0] < SCREEN_WIDTH / 2):
            self.player_drag_area = [PLAYER_ONE_BEGIN_INTERVAL, PLAYER_ONE_END_INTERVAL]
        else:
            self.player_drag_area = [PLAYER_TWO_BEGIN_INTERVAL, PLAYER_TWO_END_INTERVAL]

        super().__init__(x_position, y_position, width, height, filename)
        logging.info("End of draggable piece creation")


    # Draw the piece on the screen
    def draw(self, screen, groups):
        logging.debug("Drawing the draggable piece")
        groups.add(self.sprite)
        logging.debug("End of draggable piece draw")


    # Upadate the piece position on the screen
    def update(self, event):
        logging.debug("Updating the draggable piece")

        piece_initial_x = self.initial_board_position[0]
        piece_initial_y = self.initial_board_position[1]

        if(DraggablePiece.drag_enabled or
           ((self.get_x() != piece_initial_x) and (self.get_y() != piece_initial_y))):
            self.drag(event)
        else:
            # Do Nothing
            pass
        logging.debug("End of draggable piece update")


    # Enable or desable the drag of the pieces from the list to the board
    @classmethod
    def set_drag_enable(cls, drag_status):
        logging.info("Setting drag status")
        cls.drag_enabled = drag_status
        logging.info("Drag status is " + str(drag_status))


    # Verify if the piece is being dragged on the screen and change the piece position
    def drag(self, event):
        if(event.type == pygame.MOUSEBUTTONDOWN):
            self.mouse_position = pygame.mouse.get_pos()
            if(self.sprite.rect.collidepoint(self.mouse_position[0],
                                             self.mouse_position[1])):
                self.isDrag = True
                logging.info("Piece is being dragged")
            else:
                # Do nothing
                pass

        if(self.isDrag):
            self.mouse_position = pygame.mouse.get_pos()

            new_position = [self.mouse_position[0] - self.width / 2,
                            self.mouse_position[1] - self.height / 2]

            # Follow the mouse movement
            logging.info("Piece following the mouse")
            self.__move(new_position[0], new_position[1])
            if(event.type == pygame.MOUSEBUTTONUP):
                self.isDrag = False
                self.verify_piece_release()


    # Verify if the piece was released on a valid position
    def verify_piece_release(self):
        logging.info("Verifying if the piece was released on a valid position")
        sprite_topleft = self.sprite.rect.topleft

        """ This part of code was found on
            http://stackoverflow.com/questions/30966223/
            pygame-snap-to-grid-board-in-chess """
        for self.current_x, self.current_y in self.corners:
            hypotenuse = math.hypot(self.current_x - sprite_topleft[0],
                                    self.current_y - sprite_topleft[1])

            if(self.__verify_valid_position(sprite_topleft, hypotenuse)):
                self.__move_to_square()
                logging.info("Put the piece on the more close board square "
                             "on the left side")
                break
            else:
                self.__move_to_initial_position()


    def __move_to_initial_position(self):
        logging.info("Moving piece to initial position")
        self.set_x(self.initial_board_position[0])
        self.set_y(self.initial_board_position[1])


    def __move_to_square(self):
        logging.info("Moving piece to square")
        self.set_x(self.current_x + CENTER_OF_SQUARE)
        self.set_y(self.current_y + CENTER_OF_SQUARE)


    def __move(self, new_x_position, new_y_position):
        logging.info("Moving piece")
        self.set_x(new_x_position)
        self.set_y(new_y_position)


    def __verify_valid_position(self, sprite_topleft, hypotenuse):
        if((self.player_drag_area[0] <= sprite_topleft[0] <= self.player_drag_area[1]) and
           (GameBoard.top_spacing <= sprite_topleft[1] <= GameBoard.end_position[1]) and
           (hypotenuse <= SNAP_DISTANCE)):
            return True
        else:
            return False
