from gameEngine.Scene import *
from game.gameboard.GameBoard import *
from game.pieces.FreshMan import *
from gameEngine.Mouse import *


class MovePieceSceneTest(Scene):

    def __init__(self, name="DEFAULT", ID=0):
        super().__init__(name, ID)
        self.game_board = GameBoard(60, 60)
        self.board_start_x = self.game_board.lateral_spacing
        self.board_start_y = self.game_board.top_spacing
        self.board_end_x = self.game_board.end_position[0]
        self.board_end_y = self.game_board.end_position[1]
        self.piece_step_size = self.game_board.square_margin + self.game_board.square_size
        self.piece = FreshMan(240 + self.piece_step_size * 4, 200 + self.piece_step_size,
                              0, 0, 0, 0, 1, 0, "asdf", "asdfasdf", 50, 50,
                              "pieces/baja_pilot.png")

    def update(self, events):
        pass

    def draw(self, screen, groups):
        pass
