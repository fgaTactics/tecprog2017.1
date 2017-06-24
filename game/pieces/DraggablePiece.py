import logging
# import SquareNotFoundError
from gameEngine.GameObject import *
from game.gameboard.GameBoard import *
from gameEngine.GameEngine import SCREEN_WIDTH
from gameEngine.GameSounds import *
import math


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
    def __init__(self, x_position, y_position, width,
                 height, filename, piece_name, square=None, player=None):
        assert x_position > 0 and y_position > 0, "Can't create a piece outside vision"
        assert width > 0 and height > 0, "Can't create an invisible and inclickable piece"

        logging.info("Building draggable piece")

        self.isDrag = False

        self.actualSquare = None
        self.game_board = GameBoard.get_instance()

        self.initial_board_position = [0, 0]
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

        self.sound_button = GameSounds("sound.wav")


    # Draw the piece on the screen
    def draw(self, screen, groups):
        logging.debug("Drawing the draggable piece")
        groups.add(self.sprite)
        logging.debug("End of draggable piece draw")


    # Upadate the piece position on the screen
    def update(self, event):
        logging.debug("Updating the draggable piece")

        # The player can always drag pieces that are on the board or with the drag enabled
        if(DraggablePiece.drag_enabled or self.piece_is_on_the_board()):
            self.drag(event)
        else:
            # Do Nothing
            pass
        logging.debug("End of draggable piece update")


    # Verify if the piece is on the player list or the board to allow movements and drags
    def piece_is_on_the_board(self):

        piece_initial_x = self.initial_board_position[0]
        piece_initial_y = self.initial_board_position[1]

        if(self.get_x() != piece_initial_x) or (self.get_y() != piece_initial_y):
            return True
        else:
            return False


    # The scene enable or disable the drag of the pieces from the list to the board
    @classmethod
    def set_drag_enable(cls, drag_status):
        logging.info("Setting drag status")
        cls.drag_enabled = drag_status
        logging.info("Drag status is " + str(drag_status))


    # Verify if the piece is being dragged on the screen and change the piece position
    def drag(self, event):

        self.verify_if_piece_is_being_dragged(event)

        if(self.isDrag):
            self.__move_piece_to_mouse()

            if(event.type == pygame.MOUSEBUTTONUP):
                self.isDrag = False
                self.verify_piece_release()
            else:
                # Do nothing
                pass
        else:
            # Do nothing
            pass

    def __move_piece_to_mouse(self):
        self.mouse_position = pygame.mouse.get_pos()

        # We must centralize the piece on the mouse to facilitate drag and snap
        centralized_x = self.mouse_position[0] - self.width / 2
        centralized_y = self.mouse_position[1] - self.height / 2
        new_position = [centralized_x, centralized_y]

        # Follow the mouse movement
        logging.debug("Piece following the mouse")
        try:
            self.__move(new_position[0], new_position[1])
        except:
            # If the player tries to move to an invalid position, we reset the piece
            self.__move_to_initial_position()

    # Before we move the piece, we must assure the mouse is clicking down and on the piece
    def verify_if_piece_is_being_dragged(self, event):

        if(event.type == pygame.MOUSEBUTTONDOWN):
            self.mouse_position = pygame.mouse.get_pos()

            if(self.sprite.rect.collidepoint(self.mouse_position[0],
                                             self.mouse_position[1])):
                logging.info("Piece is being dragged")
                self.isDrag = True
                self.sound_button.play_sound()
                logging.info("Piece is being dragged")
            else:
                # Do nothing
                pass
        else:
            # Do nothing
            pass


    # Verify if the piece was released on a valid position and pull the piece to a square
    def verify_piece_release(self):
        logging.info("Verifying if the piece was released on a valid position")

        # We must clear the old square before moving the piece to a new one or the list
        self.__clearActualSquare()

            if(self.__verify_valid_position(sprite_topleft, hypotenuse)):
                self.__move_to_square()
                self.sound_button.play_sound()
                logging.info("Put the piece on the more close board square "
                             "on the left side")
                break
            else:
                self.__move_to_initial_position()


    # While the piece is being moved to a new square, the old one must be cleared
    def __clearActualSquare(self):
        # Can't clear if the piece don't have an old square
        try:
            self.actualSquare.remove_piece()
        except:
            # Do Nothing
            pass

    # Every piece has its own initial position defined by pieceListItem that created it
    def __move_to_initial_position(self):
        logging.info("Moving piece to initial position")
        self.set_x(self.initial_board_position[0])
        self.set_y(self.initial_board_position[1])

    # Used to set piece new positions following the mouse
    def __move(self, new_x_position, new_y_position):
        if(new_x_position < 0 or new_y_position < 0):
            raise ValueError
        else:
            # Do nothing
            pass

        logging.info("Moving piece")
        self.set_x(new_x_position)
        self.set_y(new_y_position)

    def get_square(self):
        return self.__square

    def set_square(self, square):
        self.__square = square

    def get_player(self):
        return self.__player

    def set_player(self, player):
        self.__player = player
