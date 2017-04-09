
from gameEngine.Sprite import *


class GameObject:

    def __init__(self, x_position, y_position, width, height, filename):
        self.sprite = Sprite(filename)
        self.width = width
        self.height = height
        self.set_x(x_position)
        self.set_y(y_position)
        self.sprite.resize(width, height)
        
    def draw(self, groups):
        groups.add(self.sprite)

    def update(self):
        pass

    def get_x(self):
        return self.sprite.image.rect.x

    def get_y(self):
        return self.sprite.image.rect.y

    def set_x(self, x_position):
        self.sprite.rect.x = x_position

    def set_y(self, y_position):
        self.sprite.rect.y = y_position
