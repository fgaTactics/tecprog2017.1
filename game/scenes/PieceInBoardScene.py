from gameEngine.Scene import *
from gameEngine.Mouse import *
from game.gameboard.GameBoard import *
from game.pieces.Engineer import *
from game.pieces.FreshMan import *
from game.pieces.Teacher import *
from game.ArmyPositionService import *
from game.gameboard.PieceMenu import *
from game.PlayerService import *
from gameEngine.GameText import *

"""This class show the pieces in the board"""

# Constants to define board's width and height
BOARD_WIDTH = 60
BOARD_HEIGHT = 60
TEXT_PLAYER_TURN_X = 500
TEXT_PLAYER_TURN_Y = 100


class PieceInBoardScene(Scene):


    pieces_in_the_board_player1 = []
    pieces_in_the_board_player2 = []

    # create two basic pieces for test
    teacher = Teacher(health=0, attack=0, rangeAttack=0, defense=0,
                      amount_of_moviment=0, penalty=0,
                      hability="", description="Teacher1", x_position=150,
                      y_position=100,
                      width=60, height=60, filename="teacher.jpg")


    teacher2 = Teacher(health=0, attack=0, rangeAttack=0, defense=0,
                       amount_of_moviment=0, penalty=0,
                       hability="", description="Teacher2", x_position=350,
                       y_position=500,
                       width=60, height=60, filename="teacher.jpg")

    PlayerService.set_player1_pieces_list(teacher)
    PlayerService.set_player2_pieces_list(teacher2)

    pieces_in_the_board_player1 = PlayerService.player1_piece_list
    pieces_in_the_board_player2 = PlayerService.player2_piece_list

    def __init__(self, name="DEFAULT", ID=0):
        super().__init__(name, ID)
        self.game_board = GameBoard(BOARD_HEIGHT)

    def draw(self, screen, groups):
        # Fill the screen with black to erase outdated screen
        screen.fill((0, 0, 0))
        self.game_board.draw(screen)

        for piece1 in self.pieces_in_the_board_player1:
            piece1.draw(screen, groups)

        for piece2 in self.pieces_in_the_board_player2:
            piece2.draw(screen, groups)

        self.show_player_turn(1)

    def update(self, events):

        count_action_player1 = 0
        count_action_player2 = 0

        for piece1 in self.pieces_in_the_board_player1:
            piece1.update(events)

        for piece2 in self.pieces_in_the_board_player2:
            piece2.update(events)

    def show_player_turn(self, player_number):
        assert player_number > 0 and player_number < 3, "out range for number player"

        if(player_number == 1):
            GameText.print("Player 1 turn", TEXT_PLAYER_TURN_X,
                           TEXT_PLAYER_TURN_Y)
        else:
            GameText.print("Player 2 turn", TEXT_PLAYER_TURN_X,
                           TEXT_PLAYER_TURN_Y)
