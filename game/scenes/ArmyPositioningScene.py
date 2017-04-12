from gameEngine.Scene import *
from game.pieces.DraggablePiece import *

class ArmyPositioningScene(Scene):

    def __init__(self, name="DEFAULT", ID=666):
        super().__init__(name, ID)
        self.test_piece = DraggablePiece(0, 0, 100, 100, "MYP.png")


    def draw(self, groups):
        groups.add(self.test_piece.sprite)


    def update(self, event):
        self.test_piece.update(event)