from gameEngine.GameObject import *
from gameEngine.Sprite import *
from gameEngine.GameText import *
import pygame


class PieceListItem(GameObject):

    def __init__(self, piece_name, x_position, y_position, width, height, filename):
        super().__init__(x_position, y_position, width, height, filename)
        self.piece_filename = self.select_piece_image(piece_name)
        self.piece_quantity = self.select_piece_quantity(piece_name)
        self.piece_icon = Sprite(self.piece_filename)
        self.piece_icon.resize(50, 50)
        self.piece_icon.set_x(self.get_x() + 10)
        self.piece_icon.set_y(self.get_y() + 10)

    def update(self, events):
        pass

    def draw(self, screen, groups):
        groups.add(self.sprite)
        groups.add(self.piece_icon)
        self.write_number_of_pieces(screen)

    def write_number_of_pieces(self, screen):
        text_x_position = self.get_x() + 85
        text_y_position = self.get_y() + 20
        GameText.print("x" + str(self.piece_quantity), text_x_position, text_y_position)

    def select_piece_quantity(self, piece_name):
        # All pieces limit quantity is defined as 2
        return 2

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
