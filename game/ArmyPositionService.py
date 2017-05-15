from Engineer import *
from FreshMan import *
from Teacher import *
from DraggablePiece import *
import logging

ARMY_SIZE = 10

""" -- This class is responsible to transform draggable pieces into
       pieces that allow us to play (attack and move on the board),
       making the player army -- """
class ArmyPositionService:

    piece_list = []

    """ Transform a list of draggable pieces into a list
    of pieces that allow us to move and attack """
    @classmethod
    def set_piece_list(cls, draggable_piece_list):
        if(len(draggable_piece_list) == ARMY_SIZE):
            cls.__refresh()
        
            for piece in draggable_piece_list:
                cls.__add_piece(piece)
        else:
            raise ValueError("The list of draggable pieces must be equal to ten")   


    @classmethod
    def get_piece_list(cls):
        return cls.piece_list

    
    # Clear the existing list of pieces
    @classmethod
    def __refresh(cls):
        logging.info("Cleaning the existing list")
        cls.piece_list[:] = []
    
        
    @classmethod
    def __add_piece(cls, piece):
        assert issubclass(type(piece), DraggablePiece), "The parameter is not a piece"
        
        if(piece.name == "Engineer"):
            new_piece = Enginneer(health=0, attack=0, rangeAttack=0, 
                                 defense=0, 
                                 amount_of_moviment=0, 
                                 penalty=0, 
                                 hability="", 
                                 description="", 
                                 x_position=0, 
                                 y_position=0, 
                                 width=0, 
                                 height=0, 
                                 filename=piece.image)
            
        elif(piece.name == "FreshMan"):
            new_piece = FreshMan(health=0, attack=0, rangeAttack=0, 
                                 defense=0, 
                                 amount_of_moviment=0, 
                                 penalty=0, 
                                 hability="", 
                                 description="", 
                                 x_position=0, 
                                 y_position=0, 
                                 width=0, 
                                 height=0, 
                                 filename=piece.image)
            
        elif(piece.name == "Teacher"):
            new_piece = Teacher(health=0, attack=0, rangeAttack=0, 
                                 defense=0, 
                                 amount_of_moviment=0, 
                                 penalty=0, 
                                 hability="", 
                                 description="", 
                                 x_position=piece.board_position[0], 
                                 y_position=piece.board_position[1], 
                                 width=piece.width, 
                                 height=piece.height, 
                                 filename=piece.image)
            
        cls.piece_list.append(new_piece)
        logging.info("Piece added to piece list")