from game.pieces.Engineer import *
from game.pieces.FreshMan import *
from game.pieces.Teacher import *
from game.pieces.DraggablePiece import *
import logging

ARMY_SIZE = 10

""" -- This class is responsible to transform draggable pieces into
       pieces that allow us to play (attack and move on the board),
       making the player army -- """


class ArmyService:

    piece_list = []
    both_player_pieces = []

    """ Transform a list of draggable pieces into a list
    of pieces that allow us to move and attack """
    @classmethod
    def set_piece_list(cls, draggable_piece_list):
        if(len(draggable_piece_list) == ARMY_SIZE):
            cls.__refresh()
            for piece in draggable_piece_list:
                cls.__add_piece(piece)

            cls.both_player_pieces.append(cls.piece_list)
        else:
            raise ValueError("The list of draggable pieces must be equal to ten")


    @classmethod
    def get_players_piece_list(cls):
        return cls.both_player_pieces


    # Clear the existing list of pieces
    @classmethod
    def __refresh(cls):
        logging.info("Cleaning the existing list")
        cls.piece_list = None
        cls.piece_list = []


    @classmethod
    def __add_piece(cls, piece):
        assert issubclass(type(piece), DraggablePiece), "The parameter is not a piece"

        if(piece.name == "engineer"):
            new_piece = Engineer(health=0, attack=0, rangeAttack=0,
                                 defense=0,
                                 amount_of_moviment=1,
                                 penalty=0,
                                 hability="",
                                 description="",
                                 x_position=piece.get_x(),
                                 y_position=piece.get_y(),
                                 width=piece.width,
                                 height=piece.height,
                                 filename=piece.image,
                                 square=piece.get_square(),
                                 player=piece.get_player())
            piece.get_square().remove_piece()
            piece.get_square().add_piece(new_piece)

        elif(piece.name == "freshman"):
            new_piece = FreshMan(health=0, attack=0, rangeAttack=0,
                                 defense=0,
                                 amount_of_moviment=2,
                                 penalty=0,
                                 hability="",
                                 description="",
                                 x_position=piece.get_x(),
                                 y_position=piece.get_y(),
                                 width=piece.width,
                                 height=piece.height,
                                 filename=piece.image,
                                 square=piece.get_square(),
                                 player=piece.get_player())
            piece.get_square().remove_piece()
            piece.get_square().add_piece(new_piece)

        elif(piece.name == "teacher"):
            new_piece = Teacher(health=0, attack=0, rangeAttack=0,
                                defense=0,
                                amount_of_moviment=2,
                                penalty=0,
                                hability="",
                                description="",
                                x_position=piece.get_x(),
                                y_position=piece.get_y(),
                                width=piece.width,
                                height=piece.height,
                                filename=piece.image,
                                square=piece.get_square(),
                                player=piece.get_player())
            piece.get_square().remove_piece()
            piece.get_square().add_piece(new_piece)
        else:
            new_piece = BasicPiece(health=0, attack=0, rangeAttack=0,
                                   defense=0,
                                   amount_of_moviment=3,
                                   penalty=0,
                                   hability="",
                                   description="",
                                   x_position=piece.get_x(),
                                   y_position=piece.get_y(),
                                   width=piece.width,
                                   height=piece.height,
                                   filename=piece.image,
                                   square=piece.get_square(),
                                   player=piece.get_player())
            piece.get_square().remove_piece()
            piece.get_square().add_piece(new_piece)

        cls.piece_list.append(new_piece)
        logging.info("Piece added to piece list")
