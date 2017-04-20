from game.pieces.BasicPiece import *

"""This class created the basic
structure for scene
"""


class Scene(object):

    def __init__(self, name="DEFAULT", ID=0):
        self.name = name
        self.ID = ID

    def update(self):
        pass

    def draw(self, groups):
        pass
