from gameEngine.Scene import *
from game.gameboard.GameBoard import *
from game.pieces.Engineer import *
from game.pieces.FreshMan import *


class PieceInBoardScene(Scene):
    pieces = []

    def __init__(self, name="DEFAULT", ID=0, pieces_list=None):
        super().__init__(name, ID)
        self.game_board = GameBoard(60, 60)
        self.pieces = pieces_list

    def draw(self, screen, groups):
        self.game_board.draw(screen)
        for a in self.pieces:
            a.draw(screen, groups)
