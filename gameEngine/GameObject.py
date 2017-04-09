
from gameEngine.Sprite import *


class GameObject:

    def __init__(self, width, height, filename):
        self.sprite = Sprite(filename)
        self.width = width
        self.height = height

    def draw(self, groups):
        groups.add(self.sprite)

    def update(self):
        pass
