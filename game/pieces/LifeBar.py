import pygame
import math
from gameEngine.GameObject import *
from gameEngine.Sprite import *


# Positions and size to pieces' life bar

LIFE_BAR_WIDTH = 50
LIFE_BAR_HEIGHT = 5
FILENAME = "blue_retangule.png"


class LifeBar(GameObject):

    def __init__(self, life_bar_position_x, life_bar_position_y, total_health):
        super().__init__(life_bar_position_x,
                         life_bar_position_y,
                         LIFE_BAR_WIDTH,
                         LIFE_BAR_HEIGHT,
                         FILENAME)
        #assert total_health > 0, "Can't create a life bar for a piece with 0 health"
        #self.total_health = total_health


    def update_life(self, actual_life):

        life_percentage = actual_life/self.total_health

        new_width = LIFE_BAR_WIDTH * life_percentage
        new_width = math.floor(new_width)

        self.sprite.resize(new_width, LIFE_BAR_HEIGHT)
        

    def draw(self, screen, groups):
        groups.add(self.sprite)
    
    def update_life_bar_position(self,life_bar_position_x,life_bar_position_y):
        self.set_x(life_bar_position_x)
        self.set_y(life_bar_position_y)
  