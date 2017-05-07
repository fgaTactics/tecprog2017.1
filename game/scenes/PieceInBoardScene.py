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
board_width = 60
board_height = 60

# Instance off menu piece
menu = PieceMenu()

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
                      hability="", description="Teacher1", x_position=150,
                      y_position=170,
                      width=60, height=60, filename="teacher.jpg")    
    
    piecesInTheBoard.append(teacher)
    piecesInTheBoard.append(teacher2)

    def __init__(self, name="DEFAULT", ID=0):
        super().__init__(name, ID)
        self.game_board = GameBoard(board_height, board_width)

    def draw(self, screen, groups):
        mouse = Mouse()
        
        self.game_board.draw(screen)

        for a in self.piecesInTheBoard:
            a.draw(screen, groups)
            
            # Verify is player is click in any piece to open option's menu    
            if(mouse.is_mouse_click(a)):
                print("Menu da peça foi aberto ! Selecione as opções")
                # Set menu positions relative to piece
                menu.set_positions(a)
                menu.is_open = True
            
            # If player clicks on piece, the menu will open
            if(menu.is_open):
                menu.draw(screen, groups)
            