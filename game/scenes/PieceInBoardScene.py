from gameEngine.Scene import *
from game.gameboard.GameBoard import *
from game.pieces.Engineer import *
from game.pieces.FreshMan import *
from game.pieces.Teacher import *
from game.ArmyPositionService import *


class PieceInBoardScene(Scene):
    
       
    piecesInTheBoard = []
    for i in range(0, 5):
        freshMan = FreshMan(health=0, attack=0, rangeAttack=0, defense=0, 
                            amount_of_moviment=0, 
                           penalty=0, hability="", 
                           description="hue", x_position=200, 
                           y_position=50, width=60, 
                           height=60, filename="MYP.png")
        
        piecesInTheBoard.append(freshMan)
    for i in range(0, 10):
        teacher = Teacher(health=0, attack=0, rangeAttack=0, defense=0, 
                          amount_of_moviment=0, penalty=0, 
                         hability="", description="hue1", x_position=150, 
                           y_position=100, 
                         width=60, height=60, filename="MYP.png")        
        piecesInTheBoard.append(teacher)
        
    for i in range(0, 5):
        engenner = Engenner(health=0, attack=0, rangeAttack=0, defense=0, 
                            amount_of_moviment=0, 
                           penalty=0, hability="", 
                           description="hue2", x_position=1, 
                           y_position=100, width=60, 
                           height=60, filename="MYP.png")
        piecesInTheBoard.append(engenner)
        
    
    def __init__(self, name="DEFAULT", ID=0):
        super().__init__(name, ID)
        self.game_board = GameBoard(60, 60)


    def draw(self, screen, groups):
        self.game_board.draw(screen)
        for a in self.piecesInTheBoard:
            a.draw(screen,groups)
            