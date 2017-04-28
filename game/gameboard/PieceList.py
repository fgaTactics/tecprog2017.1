import pygame
from gameEngine.GameObject import *
from game.pieces.DraggablePiece import *
from game.gameboard.PieceListItem import *


class PieceList(GameObject):

    def __init__(self, player_class, x_position, y_position, width, height, file_name):
        super().__init__(x_position, y_position, width, height, file_name)
        self.list_items = self.create_list_items(player_class)

    def draw(self, screen, groups):
        groups.add(self.sprite)
        for i in range(0, len(self.list_items)):
            self.list_items[i].draw(screen, groups)

    def update(self, event):
        for i in range(0, len(self.list_items)):
            self.list_items[i].update(event)

    def create_list_items(self, player_class):
        list_item_background_filename = "list_item_background.jpg"
        list_item_x_position = self.get_x() + 30
        list_item_width = 140
        list_item_height = 70
        piece_name_list = self.select_pieces(player_class)
        piece_list = []
        list_item_y_position = 40
        list_item_spacing = 15
        for i in range(0, len(piece_name_list)):
            piece_list_item = PieceListItem(piece_name_list[i], list_item_x_position,
                                            list_item_y_position,
                                            list_item_width,
                                            list_item_height,
                                            list_item_background_filename)
            piece_list.insert(i, piece_list_item)
            list_item_y_position += list_item_height + list_item_spacing
        return piece_list

    def select_pieces(self, player_class):
        piece_name_list = ["freshman", "engineer", "teacher"]

        if(player_class == "aerospace"):
            piece_name_list.append("propulsion expert")
            piece_name_list.append("cerrado elephant")
            piece_name_list.append("satellite designer")
        elif(player_class == "automotive"):
            piece_name_list.append("structural designer")
            piece_name_list.append("baja pilot")
            piece_name_list.append("the great welder")
        elif(player_class == "eletronic"):
            piece_name_list.append("vhdl programmer")
            piece_name_list.append("biomedic")
            piece_name_list.append("arduin enthusiast")
        elif(player_class == "energy"):
            piece_name_list.append("biogamense")
            piece_name_list.append("itaipu trainee")
            piece_name_list.append("matriz employee")
        elif(player_class == "software"):
            piece_name_list.append("cpd trainee")
            piece_name_list.append("java witness")
            piece_name_list.append("tep marathonist")
        else:
            # Do nothing
            pass

        return piece_name_list
