from gameEngine.GameObject import *
from gameEngine.Sprite import *
from gameEngine.GameText import *
from game.pieces.DraggablePiece import *
from game.ArmyPositionService import *

import pygame


class PieceListItem(GameObject):

    def __init__(self, piece_name, x_position, y_position, width, height, filename):
        super().__init__(x_position, y_position, width, height, filename)
        self.piece_filename = self.select_piece_image(piece_name)
        self.piece_max_quantity = self.select_piece_quantity(piece_name)
        self.piece_quantity = self.piece_max_quantity
        self.piece_icon = Sprite(self.piece_filename)
        self.pieces = []
        for i in range(0, self.piece_max_quantity):
            self.pieces.insert(i, DraggablePiece(self.get_x() + 10, self.get_y() + 10, 50,
                                                 50, self.piece_filename, self))
            self.pieces_in_the_board(self.pieces)

        self.piece_icon.resize(50, 50)
        self.piece_icon.set_x(self.get_x() + 10)
        self.piece_icon.set_y(self.get_y() + 10)

    def update(self, event):
        self.count_piece_quantity()
        for i in range(0, self.piece_max_quantity):
            if(self.piece_need_update(self.pieces[i])):
                self.pieces[i].update(event)
            else:
                # Do Nothing
                pass

    def count_piece_quantity(self):
        self.piece_quantity = self.piece_max_quantity
        for i in range(0, self.piece_max_quantity):
            if(not self.piece_is_on_list(self.pieces[i])):
                self.piece_quantity -= 1
            else:
                # Do nothing
                pass

    def piece_need_update(self, piece):
            if(self.piece_is_on_list(piece)):
                if(self.piece_index_is_max(piece)):
                    return True
                else:
                    return False
            else:
                return True

    def pieces_in_the_board(self, pieces):
        list_piece_on_the_board = []
        index = 0
        print("hueueh", len(pieces))
        for index in range(0, len(pieces)):
            if(self.piece_is_on_list(pieces[index])):
                list_piece_on_the_board.append(pieces[index])

        ArmyPositionService.set_piece_list(list_piece_on_the_board)
        print("tamanho", len(ArmyPositionService.get_piece_list()))


    def piece_index_is_max(self, piece):
        max_index = 0
        for i in range(0, self.piece_max_quantity):
            if(self.piece_is_on_list(self.pieces[i])):
                max_index = i
        if(self.pieces.index(piece) == max_index):
            return True
        else:
            return False

    def piece_is_on_list(self, piece):
        if(piece.get_x() > self.get_x() and
           piece.get_x() < self.get_x() + self.width):
            return True
        else:
            return False

    def draw(self, screen, groups):
        groups.add(self.sprite)
        groups.add(self.piece_icon)
        self.write_number_of_pieces(screen)
        for i in range(0, self.piece_max_quantity):
            self.pieces[i].draw(screen, groups)

    def write_number_of_pieces(self, screen):
        text_x_position = self.get_x() + 85
        text_y_position = self.get_y() + 20
        GameText.print("x" + str(self.piece_quantity), text_x_position, text_y_position)


    def select_piece_quantity(self, piece_name):
        # All pieces limit quantity is defined as 2
        return 4

    def select_piece_image(self, piece_name):
        pieces_images = {"engineer": "pieces/engineer.jpg",
                         "freshman": "pieces/freshman.jpg",
                         "teacher": "pieces/teacher.jpg",

                         # Aeroespace Engineering pieces
                         "propulsion expert": "pieces/propulsion_expert.png",
                         "cerrado elephant": "pieces/cerrado_elephant.png",
                         "satellite designer": "pieces/satellite_designer.png",

                         # Automotive Engineering pieces
                         "structural designer": "pieces/structural_designer.png",
                         "baja pilot": "pieces/baja_pilot.png",
                         "the great welder": "pieces/the_great_welder.png",

                         # Eletronic Engineering pieces
                         "vhdl programmer": "pieces/vhdl_programmer.png",
                         "biomedic": "pieces/biomedic.png",
                         "arduin enthusiast": "pieces/arduin_enthusiast.png",

                         # Energy Engineering pieces
                         "biogamense": "pieces/biogamense.jpg",
                         "itaipu trainee": "pieces/itaipu_trainee.jpg",
                         "matriz employee": "pieces/matriz_employee.jpg",

                         # Software Engineering pieces
                         "cpd trainee": "pieces/cpd_trainee.jpg",
                         "java witness": "pieces/java_witness.jpg",
                         "tep marathonist": "pieces/tep_marathonist.jpg"}

        return pieces_images.get(piece_name, "Not Found")
