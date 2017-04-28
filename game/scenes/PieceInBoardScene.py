from gameEngine.Scene import *
from game.gameboard.GameBoard import *
from game.pieces.Engineer import *


class PieceInBoardScene(Scene):
    engener = Engenner(health=0, attack=0, rangeAttack=0, defense=0,
                       amount_of_moviment=0, penalty=0,
                       hability="", description="",
                       x_position=0, y_position=0,
                       width=60, height=60, filename="MYP.png")

    def __init__(self, name="DEFAULT", ID=0):
        super().__init__(name, ID)
        self.game_board = GameBoard(60, 60)


    def draw(self, screen, groups):
        self.game_board.draw(screen)
        self.engener.draw(screen, groups)
