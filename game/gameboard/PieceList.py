import pygame
from gameEngine.GameObject import *
from game.pieces.DraggablePiece import *


class PieceList(GameObject):

    def __init__(self, player_class, x_position, y_position, width, height, file_name):
        super().__init__(x_position, y_position, width, height, file_name)


    def draw(self, groups):
        groups.add(self.sprite)


    def update(self, event):
        pass
