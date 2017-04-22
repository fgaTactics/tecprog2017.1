from gameEngine.Scene import *
from game.pieces.DraggablePiece import *
from game.gameboard.GameBoard import *


class ArmyPositioningScene(Scene):

    def __init__(self, name="DEFAULT", ID=0):
        super().__init__(name, ID)
        self.test_piece = DraggablePiece(0, 0, 50, 50, "MYP.png")
        self.game_board = GameBoard(60, 60)

    def draw(self, screen, groups):
        screen.fill((0, 0, 0))
        groups.add(self.test_piece.sprite)
        self.game_board.draw(screen)

    def update(self, event):
        self.test_piece.update(event)
