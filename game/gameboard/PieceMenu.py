import pygame
from gameEngine.GameObject import *
from gameEngine.Mouse import *

# RGB color definitions
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# Positions and size to pieces' menu in pixel units
PIECE_MENU_POSITION_X = -5
PIECE_MENU_POSITION_Y = 170
PIECE_MENU_WIDTH = 200
PIECE_MENU_HEIGHT = 363
FILENAME = "MYP.png"

# Buttons within menu positions in pixel units
BUTTON_WIDTH = 120
BUTTON_HEIGHT = 80
BUTTON_VERTICAL_SPACING = 45
SPACING = 10
ATTACK_BUTTON_FILENAME = "attack_inactive.png"
MOVE_BUTTON_FILENAME = "move_inactive.png"
CANCEL_BUTTON_FILENAME = "cancel_inactive.png"

""" This class is responsable to manager the piece menu at the screen
when click on piece """


class PieceMenu(GameObject):

    is_open = False
    piece_menu_instance = None


    def __init__(self):
        super().__init__(PIECE_MENU_POSITION_X,
                         PIECE_MENU_POSITION_Y,
                         PIECE_MENU_WIDTH,
                         PIECE_MENU_HEIGHT,
                         FILENAME)

        self.attack_button = GameObject(self.get_x() +
                                        ((PIECE_MENU_WIDTH - BUTTON_WIDTH) / 2),
                                        self.get_y() + BUTTON_VERTICAL_SPACING,
                                        BUTTON_WIDTH,
                                        BUTTON_HEIGHT,
                                        ATTACK_BUTTON_FILENAME)

        self.movement_button = GameObject(self.get_x() +
                                          ((PIECE_MENU_WIDTH - BUTTON_WIDTH) / 2),
                                          self.get_y() + BUTTON_HEIGHT +
                                          BUTTON_VERTICAL_SPACING + SPACING,
                                          BUTTON_WIDTH,
                                          BUTTON_HEIGHT,
                                          MOVE_BUTTON_FILENAME)

        self.cancel_button = GameObject(self.get_x() +
                                        ((PIECE_MENU_WIDTH - BUTTON_WIDTH) / 2),
                                        self.get_y() + 2 * BUTTON_HEIGHT +
                                        BUTTON_VERTICAL_SPACING + SPACING * 2,
                                        BUTTON_WIDTH,
                                        BUTTON_HEIGHT,
                                        CANCEL_BUTTON_FILENAME)

        PieceMenu.piece_menu_instance = self
        self.is_open = False

    def set_positions(self, x_position):
        self.set_x(x_position)
        self.attack_button.set_x(x_position + ((PIECE_MENU_WIDTH - BUTTON_WIDTH) / 2))
        self.movement_button.set_x(x_position + ((PIECE_MENU_WIDTH - BUTTON_WIDTH) / 2))
        self.cancel_button.set_x(x_position + ((PIECE_MENU_WIDTH - BUTTON_WIDTH) / 2))
        self.set_y(PIECE_MENU_POSITION_Y)

    def open(self):
        self.is_open = True

    def close(self):
        self.is_open = False

    def is_open(self):
        return self.is_open

    def draw(self, screen, groups):
        if(self.is_open):
            groups.add(self.sprite)
            groups.add(self.attack_button.sprite)
            groups.add(self.movement_button.sprite)
            groups.add(self.cancel_button.sprite)

    @classmethod
    def get_piece_menu(cls):
        return cls.piece_menu_instance
