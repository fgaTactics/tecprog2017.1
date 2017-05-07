""" This class is responsable to manager the piece menu at the screen
when click on piece """

import pygame
from gameEngine.GameObject import *

# RGB color definitions
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# Positions and size to pieces' menu
PIECE_MENU_POSITION_X = 0
PIECE_MENU_POSITION_Y = 0
PIECE_MENU_WIDTH = 100
PIECE_MENU_HEIGHT = 100
FILENAME = "MYP.png"

class PieceMenu(GameObject):

    is_open = False
    
    def __init__(self):
        super().__init__(PIECE_MENU_POSITION_X,
                         PIECE_MENU_POSITION_Y,
                         PIECE_MENU_WIDTH,
                         PIECE_MENU_HEIGHT,
                         FILENAME)
    
    def set_positions(self, piece):
        self.set_x(piece.get_x() + 20)
        self.set_y(piece.get_y() + 20)
