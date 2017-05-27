import pygame
from gameEngine.GameObject import *



# Positions and size to pieces' life bar

LIFE_BAR_WIDTH = 50
LIFE_BAR = 15
FILENAME = "blue_retangule.png"


class LifeBar(GameObject):

    def __init__(self, life_bar_position_x, life_bar_position_y):
        super().__init__(life_bar_position_x,
                         life_bar_position_y,
                         LIFE_BAR_WIDTH,
                         LIFE_BAR,
                         FILENAME)



    def draw(self, screen, groups):
        groups.add(self.sprite)
