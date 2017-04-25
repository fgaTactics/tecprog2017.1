from gameEngine.Scene import *
from game.gameboard.GameBoard import *
from game.gameboard.PieceList import *
from game.PlayerService import *


class ArmyPositioningScene(Scene):

    def __init__(self, name="DEFAULT", ID=0):
        super().__init__(name, ID)
        self.game_board = GameBoard(60, 60)

    def load(self):
        player1_class = PlayerService.get_player(0)
        player2_class = PlayerService.get_player(1)
        self.left_piece_list = PieceList(player1_class, 0, 0, 200, 800, "PieceMenu.png")
        self.right_piece_list = PieceList(player2_class, 1000, 0, 200, 800,
                                          "PieceMenu.png")

    def draw(self, screen, groups):
        screen.fill((0, 0, 0))
        self.game_board.draw(screen)
        self.left_piece_list.draw(screen, groups)
        self.right_piece_list.draw(screen, groups)

    def update(self, event):
        self.right_piece_list.update(event)
        self.left_piece_list.update(event)
