from gameEngine.GameObject import *
from game.gameboard.GameBoard import *
from gameEngine.GameEngine import SCREEN_WIDTH
import math

""" -- This class is used to move pieces to form the player army  -- """

# Distance to pull the piece into a valid square
SNAP_DISTANCE = GameBoard.square_size / 2 + GameBoard.square_margin

# Distance to centralize the piece into square of the board
CENTER_OF_SQUARE = 20


class DraggablePiece(GameObject):


    def __init__(self, x_position, y_position, width, height, filename, pieceListItem):
        self.pieceListItem = pieceListItem
        self.isDrag = False
        self.mousePosition = [0, 0]
        self.corners = []

        self.initial_piece_position = [0, 0]
        self.board_positions = [0, 0]

        # Valid drag area for both players
        self.player_one_drag_area = [232, 337]
        self.player_two_drag_area = [802, 967]

        # Define the board space
        for x in range(GameBoard.lateral_spacing, GameBoard.end_position[0],
                       GameBoard.square_size + GameBoard.square_margin):
            for y in range(GameBoard.top_spacing, GameBoard.end_position[1],
                           GameBoard.square_size + GameBoard.square_margin):

                self.corners.append((x, y))

        self.initial_piece_position[0] = x_position
        self.initial_piece_position[1] = y_position

        super().__init__(x_position, y_position, width, height, filename)

    def draw(self, screen, groups):
        groups.add(self.sprite)

    def update(self, event):
        self.drag(event)


    """ Verify if the piece is being draged on the screen
        and change the piece position """
    def drag(self, event):
        if(event.type == pygame.MOUSEBUTTONDOWN):
            self.mouse_position = pygame.mouse.get_pos()
            if(self.sprite.rect.collidepoint(self.mouse_position[0],
                                             self.mouse_position[1])):
                self.isDrag = True
        elif(event.type == pygame.MOUSEBUTTONUP):
            self.isDrag = False

        if(self.isDrag):
            self.mouse_position = pygame.mouse.get_pos()
            self.set_x(self.mouse_position[0] - self.width / 2)
            self.set_y(self.mouse_position[1] - self.height / 2)

        else:
            self.verify_drag()


    # Verify if the piece was released on a valid position
    def verify_drag(self):
        sprite_topleft = self.sprite.rect.topleft

        for self.board_positions[0], self.board_positions[1] in self.corners:
            hypotenuse = math.hypot(self.board_positions[0] - sprite_topleft[0],
                                    self.board_positions[1] - sprite_topleft[1])

            if(self.initial_piece_position[0] < SCREEN_WIDTH / 2):
                if((self.player_one_drag_area[0] <= sprite_topleft[0] <=
                    self.player_one_drag_area[1]) and
                   (GameBoard.top_spacing <= sprite_topleft[1] <=
                    GameBoard.end_position[1]) and
                   (hypotenuse <= SNAP_DISTANCE)):

                    self.set_x(self.board_positions[0] + CENTER_OF_SQUARE)
                    self.set_y(self.board_positions[1] + CENTER_OF_SQUARE)
                    break
                else:

                    self.set_x(self.initial_piece_position[0])
                    self.set_y(self.initial_piece_position[1])
            else:
                if((self.player_two_drag_area[0] <= sprite_topleft[0] <=
                    self.player_two_drag_area[1]) and
                   (GameBoard.top_spacing <= sprite_topleft[1] <=
                    GameBoard.end_position[1]) and
                   (hypotenuse <= SNAP_DISTANCE)):

                    self.set_x(self.board_positions[0] + CENTER_OF_SQUARE)
                    self.set_y(self.board_positions[1] + CENTER_OF_SQUARE)
                    break
                else:
                    self.set_x(self.initial_piece_position[0])
                    self.set_y(self.initial_piece_position[1])
