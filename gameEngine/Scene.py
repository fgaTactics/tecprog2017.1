from game.pieces.BasicPiece import *


class Scene(object):

    def __init__(self, name="DEFAULT", ID=0):
        self.name = name
        self.ID = ID

    def update(self):
        pass

    def draw(self, groups):
        pass
