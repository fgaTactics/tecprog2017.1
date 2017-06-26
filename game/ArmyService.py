from game.pieces.Engineer import *
from game.pieces.DraggablePiece import *
from game.pieces.FreshMan import *
from game.pieces.ArduinEnthusiast import *
from game.pieces.BajaPilot import *
from game.pieces.Biogamense import *
from game.pieces.Biomedic import *
from game.pieces.CerradoElephant import *
from game.pieces.CpdTrainee import *
from game.pieces.ItaipuTrainee import *
from game.pieces.JavaWitness import *
from game.pieces.MatrizEmployee import *
from game.pieces.PropulsionExpert import *
from game.pieces.SatelliteDesigner import *
from game.pieces.StructuralDesigner import *
from game.pieces.Teacher import *
from game.pieces.TepMarathonist import *
from game.pieces.TheGreatWelder import *
from game.pieces.VhdlProgrammer import *

import logging

ARMY_SIZE = 2

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
            raise ValueError("The list of draggable pieces must be equal to " + ARMY_SIZE)


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
            new_piece = Engineer(x_position=piece.get_x(),
                                 y_position=piece.get_y(),
                                 width=piece.get_width(),
                                 height=piece.get_height(),
                                 player=piece.get_player(),
                                 square=piece.get_square())
        elif(piece.name == "freshman"):
            new_piece = FreshMan(x_position=piece.get_x(),
                                 y_position=piece.get_y(),
                                 width=piece.get_width(),
                                 height=piece.get_height(),
                                 player=piece.get_player(),
                                 square=piece.get_square())

        elif(piece.name == "teacher"):
            new_piece = Teacher(x_position=piece.get_x(),
                                y_position=piece.get_y(),
                                width=piece.get_width(),
                                height=piece.get_height(),
                                player=piece.get_player(),
                                square=piece.get_square())
        elif(piece.name == "propulsion expert"):
            new_piece = PropulsionExpert(x_position=piece.get_x(),
                                         y_position=piece.get_y(),
                                         width=piece.get_width(),
                                         height=piece.get_height(),
                                         player=piece.get_player(),
                                         square=piece.get_square())
        elif(piece.name == "cerrado elephant"):
            new_piece = CerradoElephant(x_position=piece.get_x(),
                                        y_position=piece.get_y(),
                                        width=piece.get_width(),
                                        height=piece.get_height(),
                                        player=piece.get_player(),
                                        square=piece.get_square())
        elif(piece.name == "satellite designer"):
            new_piece = SatelliteDesigner(x_position=piece.get_x(),
                                          y_position=piece.get_y(),
                                          width=piece.get_width(),
                                          height=piece.get_height(),
                                          player=piece.get_player(),
                                          square=piece.get_square())
        elif(piece.name == "structural designer"):
            new_piece = StructuralDesigner(x_position=piece.get_x(),
                                           y_position=piece.get_y(),
                                           width=piece.get_width(),
                                           height=piece.get_height(),
                                           player=piece.get_player(),
                                           square=piece.get_square())
        elif(piece.name == "baja pilot"):
            new_piece = BajaPilot(x_position=piece.get_x(),
                                  y_position=piece.get_y(),
                                  width=piece.get_width(),
                                  height=piece.get_height(),
                                  player=piece.get_player(),
                                  square=piece.get_square())
        elif(piece.name == "the great welder"):
            new_piece = TheGreatWelder(x_position=piece.get_x(),
                                       y_position=piece.get_y(),
                                       width=piece.get_width(),
                                       height=piece.get_height(),
                                       player=piece.get_player(),
                                       square=piece.get_square())
        elif(piece.name == "vhdl programmer"):
            new_piece = VhdlProgrammer(x_position=piece.get_x(),
                                       y_position=piece.get_y(),
                                       width=piece.get_width(),
                                       height=piece.get_height(),
                                       player=piece.get_player(),
                                       square=piece.get_square())
        elif(piece.name == "biomedic"):
            new_piece = Biomedic(x_position=piece.get_x(),
                                 y_position=piece.get_y(),
                                 width=piece.get_width(),
                                 height=piece.get_height(),
                                 player=piece.get_player(),
                                 square=piece.get_square())
        elif(piece.name == "arduin enthusiast"):
            new_piece = ArduinEnthusiast(x_position=piece.get_x(),
                                         y_position=piece.get_y(),
                                         width=piece.get_width(),
                                         height=piece.get_height(),
                                         player=piece.get_player(),
                                         square=piece.get_square())
        elif(piece.name == "biogamense"):
            new_piece = BioGamense(x_position=piece.get_x(),
                                   y_position=piece.get_y(),
                                   width=piece.get_width(),
                                   height=piece.get_height(),
                                   player=piece.get_player(),
                                   square=piece.get_square())
        elif(piece.name == "itaipu trainee"):
            new_piece = ItaipuTrainee(x_position=piece.get_x(),
                                      y_position=piece.get_y(),
                                      width=piece.get_width(),
                                      height=piece.get_height(),
                                      player=piece.get_player(),
                                      square=piece.get_square())
        elif(piece.name == "matriz employee"):
            new_piece = MatrizEmployee(x_position=piece.get_x(),
                                       y_position=piece.get_y(),
                                       width=piece.get_width(),
                                       height=piece.get_height(),
                                       player=piece.get_player(),
                                       square=piece.get_square())
        elif(piece.name == "cpd trainee"):
            new_piece = CpdTrainee(x_position=piece.get_x(),
                                   y_position=piece.get_y(),
                                   width=piece.get_width(),
                                   height=piece.get_height(),
                                   player=piece.get_player(),
                                   square=piece.get_square())
        elif(piece.name == "java witness"):
            new_piece = JavaWitness(x_position=piece.get_x(),
                                    y_position=piece.get_y(),
                                    width=piece.get_width(),
                                    height=piece.get_height(),
                                    player=piece.get_player(),
                                    square=piece.get_square())
        elif(piece.name == "tep marathonist"):
            new_piece = TepMarathonist(x_position=piece.get_x(),
                                       y_position=piece.get_y(),
                                       width=piece.get_width(),
                                       height=piece.get_height(),
                                       player=piece.get_player(),
                                       square=piece.get_square())
        else:
            # Do Nothing
            pass

        assert ('new_piece' in locals()), "No New Piece where created, name invalid"

        piece.get_square().remove_piece()
        piece.get_square().add_piece(new_piece)

        cls.piece_list.append(new_piece)
        logging.info("Piece added to piece list")
