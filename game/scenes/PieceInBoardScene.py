import logging
from gameEngine.Scene import *
from gameEngine.Mouse import *
from game.gameboard.GameBoard import *
from game.pieces.Engineer import *
from game.pieces.FreshMan import *
from game.pieces.Teacher import *
from game.ArmyService import *
from game.gameboard.PieceMenu import *
from game.PlayerService import *
from gameEngine.GameText import *

"""This class show the pieces in the board"""

# Constants to define board's width and height
BOARD_WIDTH = 60
BOARD_HEIGHT = 60
TEXT_PLAYER_TURN_X = 500
TEXT_PLAYER_TURN_Y = 100
PLAYER_ONE = 1
PLAYER_TWO = 2
COLOR_BLACK = (0, 0, 0)


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
        screen.fill(COLOR_BLACK)

        # Calculate time for change turn
        start_ticks = pygame.time.get_ticks()

        self.game_board.draw(screen)

        for player_pieces in self.pieces_in_the_board:
            for piece in player_pieces:
                piece.draw(screen, groups)
        if(start_ticks < 5000):
            self.show_player_turn(PLAYER_ONE)
        else:
            self.show_player_turn(PLAYER_TWO)

        for piece1 in self.pieces_in_the_board_player1:
            piece1.draw(screen, groups)

        for piece2 in self.pieces_in_the_board_player2:
            piece2.draw(screen, groups)

        # to do how get action for menager turns

    def update(self, events):
        for player_pieces in self.pieces_in_the_board:
            for piece in player_pieces:
                piece.update(events)
        self.manage_player_turn(events)


    def show_player_turn(self, player_number):
        assert player_number > 0 and player_number < 3, "out range for number player"

        if(player_number == PLAYER_ONE):
            GameText.print("Player 1 turn", TEXT_PLAYER_TURN_X,
                           TEXT_PLAYER_TURN_Y)
            logging.info("Player1 turn")
        else:
            GameText.print("Player 2 turn", TEXT_PLAYER_TURN_X,
                           TEXT_PLAYER_TURN_Y)
            logging.info("Player2 turn")

    # Use the time turn while actions piece is not ready
    def manage_player_turn(self, events):

        # Calculate time for change turn
        start_ticks = pygame.time.get_ticks()

        if(start_ticks < 5000):

            for piece1 in self.pieces_in_the_board_player1:
                piece1.update(events)
            logging.info("turn time player1", start_ticks)

        elif(start_ticks > 5000 and start_ticks < 10000):

            for piece2 in self.pieces_in_the_board_player2:
                piece2.update(events)

            logging.info("turn time player2", start_ticks)
        else:
            # Nothing to do
            pass
