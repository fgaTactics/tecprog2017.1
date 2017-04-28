from gameEngine.Scene import *
from game.gameboard.GameBoard import *
from game.pieces.Engineer import *
from game.pieces.FreshMan import *
from game.ArmyPositionService import *


class PieceInBoardScene(Scene):
    pieces1 = []

    def __init__(self, name="DEFAULT", ID=0):
        super().__init__(name, ID)
        self.game_board = GameBoard(60, 60)
        self.pieces1 = ArmyPositionService.get_player_list


    def draw(self, screen, groups):
        self.game_board.draw(screen)
        for a in self.pieces1:
            a.draw(screen, groups)
