from gameEngine.Scene import *
from game.pieces.DraggablePiece import *
from game.pieces.GameBoard import *

class ArmyPositioningScene(Scene):

    def __init__(self, name="DEFAULT", ID=0):
        super().__init__(name, ID)
        self.test_piece = DraggablePiece(600, 600, 200, 200, "logo.png")
        #self.game_board = GameBoard(60,60,15)

    def draw(self,screen,groups):
        groups.add(self.test_piece.sprite)
        #self.game_board.draw(screen)
        
    def update(self, event):
        self.test_piece.update(event)
        #self.game_board.update(event)
        