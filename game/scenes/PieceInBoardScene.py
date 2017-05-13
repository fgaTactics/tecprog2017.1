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


    piecesInTheBoard = []


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

    piecesInTheBoard.append(teacher)
    piecesInTheBoard.append(teacher2)

    def __init__(self, name="DEFAULT", ID=0):
        super().__init__(name, ID)
        self.game_board = GameBoard(BOARD_HEIGHT)

    def draw(self, screen, groups):
        # Fill the screen with black to erase outdated screen
        screen.fill((0, 0, 0))
        self.game_board.draw(screen)

        for piece in self.piecesInTheBoard:
            piece.draw(screen, groups)

        self.show_player_turn(1)

    def update(self, events):
        for piece in self.piecesInTheBoard:
            piece.update(events)

    def show_player_turn(self, player_number):
        GameText.print("Player 1 turn", TEXT_PLAYER_TURN_X,
                       TEXT_PLAYER_TURN_Y)
