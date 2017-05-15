from gameEngine.Scene import *
from gameEngine.Mouse import *
from game.gameboard.GameBoard import *
from game.pieces.Engineer import *
from game.pieces.FreshMan import *
from game.pieces.Teacher import *
from game.ArmyService import *
from game.gameboard.PieceMenu import *

"""This class show the pieces in the board"""

# Constants to define board's width and height
BOARD_WIDTH = 60
BOARD_HEIGHT = 60


class PieceInBoardScene(Scene):

    def __init__(self, name="DEFAULT", ID=0):
        super().__init__(name, ID)
        self.game_board = GameBoard(BOARD_HEIGHT)
        self.pieces_in_the_board = []

    def load(self):
        both_player_pieces = ArmyService.get_players_piece_list()
        player1_army = both_player_pieces[0]
        player2_army = both_player_pieces[1]
        self.pieces_in_the_board.append(player1_army)
        self.pieces_in_the_board.append(player2_army)

    def draw(self, screen, groups):
        # Fill the screen with black to erase outdated screen
        screen.fill((0, 0, 0))
        self.game_board.draw(screen)

        for player_pieces in self.pieces_in_the_board:
            for piece in player_pieces:
                piece.draw(screen, groups)

    def update(self, events):
        for player_pieces in self.pieces_in_the_board:
            for piece in player_pieces:
                piece.update(events)
