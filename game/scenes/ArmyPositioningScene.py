from gameEngine.Scene import *
from game.gameboard.GameBoard import *
from game.gameboard.PieceList import *


class ArmyPositioningScene(Scene):

    def __init__(self, name="DEFAULT", ID=0):

        super().__init__(name, ID)
        self.game_board = GameBoard(60, 60)
        self.left_piece_list = PieceList("software", 0, 0, 200, 800, "PieceMenu.png")
        self.right_piece_list = PieceList("software", 1000, 0, 200, 800, "PieceMenu.png")
        self.test_piece = DraggablePiece(0, 0, 50, 50, "MYP.png")

    def draw(self, screen, groups):
        screen.fill((0, 0, 0))
        self.game_board.draw(screen)
        groups.add(self.left_piece_list.sprite)
        groups.add(self.right_piece_list.sprite)
        groups.add(self.test_piece.sprite)

    def update(self, event):

        self.right_piece_list.update(event)
        self.left_piece_list.update(event)
        self.test_piece.update(event)
