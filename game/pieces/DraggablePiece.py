from gameEngine.GameObject import *
from game.gameboard.GameBoard import *
import math

SIDE_OF_THE_SQUARE = 75
BEGINNING_OF_THE_BOARD = 982
END_OF_THE_BOARD = 555
# Middle of square plus margin between square
SNAP_DISTANCE = 45

INITIAL_POSITION_X = 0
INITIAL_POSITION_Y = 0

# Positions for the object position out of board
POSITION_OUT_OF_BOARD_X = 237
POSITION_OUT_OF_BOARD_Y = 200
SECOND_POSITION_OT_OF_BOARD_X = 987
SECOND_POSITION_OT_OF_BOARD_y = 520


class DraggablePiece(GameObject):

    isDrag = False
    mousePosition = [0, 0]
    corners = []

    def __init__(self, x_position, y_position, width, height, filename):

        # Define the board space
        for x in range(GameBoard.lateralSpaceColumn, BEGINNING_OF_THE_BOARD,
                       SIDE_OF_THE_SQUARE):
            for y in range(GameBoard.lateralSpaceRow, END_OF_THE_BOARD,
                           SIDE_OF_THE_SQUARE):
                self.corners.append((x, y))

        super().__init__(x_position, y_position, width, height, filename)

    def update(self, event):
        self.drag(event)

    # Verify if the piece is being draged on the screen
    # and change the piece position

    def drag(self, event):

        if(event.type == pygame.MOUSEBUTTONDOWN):
            self.mouse_position = pygame.mouse.get_pos()
            if(self.sprite.rect.collidepoint(self.mouse_position[0],
                                             self.mouse_position[1])):
                self.isDrag = True
        elif(event.type == pygame.MOUSEBUTTONUP):
            self.isDrag = False
        else:
            # Do nothing
            pass
        if(self.isDrag):
            self.mouse_position = pygame.mouse.get_pos()
            self.set_x(self.mouse_position[0] - self.width / 2)
            self.set_y(self.mouse_position[1] - self.height / 2)
        else:
            OBJECT_POSITION_X, OBJECT_POSITION_Y = self.sprite.rect.topleft
            print(self.sprite.rect.topleft)
            for BOARD_POSITION_X, BOARD_POSITION_Y in self.corners:
                if math.hypot(BOARD_POSITION_X - OBJECT_POSITION_X,
                              BOARD_POSITION_Y -
                              OBJECT_POSITION_Y) <= SNAP_DISTANCE:
                    self.set_x(BOARD_POSITION_X + 20)
                    self.set_y(BOARD_POSITION_Y + 20)
                    break
                elif (OBJECT_POSITION_Y < POSITION_OUT_OF_BOARD_Y or
                      OBJECT_POSITION_X < POSITION_OUT_OF_BOARD_X or OBJECT_POSITION_X >
                      SECOND_POSITION_OT_OF_BOARD_X or OBJECT_POSITION_Y >
                      SECOND_POSITION_OT_OF_BOARD_y):
                    self.set_x(INITIAL_POSITION_X)
                    self.set_y(INITIAL_POSITION_Y)
                    break
                else:
                    # Do nothing
                    pass
