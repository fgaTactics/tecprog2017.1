from gameEngine.Scene import *
from gameEngine.Mouse import *
from game.gameboard.GameBoard import *
from game.pieces.Engineer import *
from game.pieces.FreshMan import *
from game.pieces.Teacher import *
from game.ArmyPositionService import *
from game.gameboard.PieceMenu import *

"""This class show the pieces in the board"""

# Constants to define board's width and height
BOARD_WIDTH = 60
BOARD_HEIGHT = 60


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
                       hability="", description="Teacher2", x_position=150,
                       y_position=170,
                       width=60, height=60, filename="teacher.jpg")

    piecesInTheBoard.append(teacher)
    piecesInTheBoard.append(teacher2)

    def __init__(self, name="DEFAULT", ID=0):
        super().__init__(name, ID)
        self.game_board = GameBoard(BOARD_HEIGHT, BOARD_WIDTH)

    def draw(self, screen, groups):
        # Fill the screen with black to erase outdated screen
        screen.fill((0, 0, 0))
        self.game_board.draw(screen)

        for piece in self.piecesInTheBoard:
            piece.draw(screen, groups)
