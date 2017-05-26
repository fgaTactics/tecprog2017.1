import logging
import pygame
from gameEngine.Scene import *
from game.gameboard.GameBoard import *
from game.pieces.FreshMan import *
from gameEngine.Mouse import *

# Piece attributes values
# Numeric values in generic units
HEALTH = 0
ATTACK = 0
RANGE_ATTACK = 1
DEFENSE = 0
AMOUNT_OF_MOVIMENT = 2
PENALTY = 0
HABILITY = ""
DESCRIPTION = ""
FILENAME = "pieces/baja_pilot.png"
FILENAME2 = "pieces/freshman.jpg"
# Piece size in pixel units
WIDTH = 50
HEIGHT = 50

# Board attributes in pixel units
SQUARE_SIDE = 60
BOARD_LEFT_LIMIT = 240
BOARD_TOP_LIMIT = 200


class MovePieceScene(Scene):

    def __init__(self, name="DEFAULT", ID=0):
        logging.info("Constructing Move Piece Scene")

        super().__init__(name, ID)

        self.game_board = GameBoard(SQUARE_SIDE)

        # Space between board spaces
        self.board_start_x = self.game_board.lateral_spacing
        self.board_start_y = self.game_board.top_spacing

        # Board left and bottom limits, respectively
        self.board_end_x = self.game_board.end_position[0]
        self.board_end_y = self.game_board.end_position[1]

        # Traveled space in a piece "step" (single space moviment)
        self.piece_step_size = self.game_board.square_margin + self.game_board.square_size

        self.piece = FreshMan(HEALTH, ATTACK, RANGE_ATTACK, DEFENSE,
                              AMOUNT_OF_MOVIMENT, PENALTY, HABILITY,
                              DESCRIPTION, self.game_board.board[2][4].initial_x_position,
                              self.game_board.board[2][4].initial_y_position,
                              WIDTH, HEIGHT, FILENAME)
        self.game_board.board[2][4].add_piece(self.piece)

        self.piece2 = FreshMan(HEALTH, ATTACK, RANGE_ATTACK, DEFENSE,
                               AMOUNT_OF_MOVIMENT, PENALTY, HABILITY, DESCRIPTION,
                               self.game_board.board[2][6].initial_x_position,
                               self.game_board.board[2][6].initial_y_position, WIDTH,
                               HEIGHT, FILENAME2)
        self.game_board.board[2][6].add_piece(self.piece2)

        self.movement_enabler = False
        self.selected_piece = None
        self.previous_square = None

        logging.info("Move Piece Scene is ready")


    # Define piece movements
    def update(self, event):
        logging.debug("Beginning Move Piece scene's update method")

        if(self.selected_piece is not None):
            self.set_second_square(event, self.previous_square)
        else:
            self.previous_square = self.set_first_square(event)

        logging.debug("Finishing Move Piece scene's update method")

    def get_clicked_square(self, event):
        for row in range(self.game_board.amount_of_rows):
            for column in range(self.game_board.amount_of_columns):
                square = self.game_board.board[row][column]
                rectangle = pygame.Rect(square.initial_x_position,
                                        square.initial_y_position,
                                        square.side,
                                        square.side)

                if(event.type == pygame.MOUSEBUTTONUP):
                    mouse_position = pygame.mouse.get_pos()

                    if(rectangle.collidepoint(mouse_position[0], mouse_position[1])):
                        return (row, column)

    def calculate_range(self, x_piece_coordinate, x_coordinate,
                        y_piece_coordinate, y_coordinate):
        piece_range = (abs(x_piece_coordinate - x_coordinate) +
                       abs(y_piece_coordinate - y_coordinate))

        return piece_range

    def paint_range(self, x_piece_coordinate, y_piece_coordinate, piece_range, color):
        for x_coordinate in range(x_piece_coordinate - piece_range,
                                  x_piece_coordinate + piece_range + 1):
            for y_coordinate in range(y_piece_coordinate - piece_range,
                                      y_piece_coordinate + piece_range + 1):
                # Quantity of movement
                movement = self.calculate_range(x_piece_coordinate, x_coordinate,
                                                y_piece_coordinate, y_coordinate)
                if(movement <= piece_range):
                    if(self.verify_board_limits(x_coordinate, y_coordinate)):
                        current_square = self.game_board.board[x_coordinate][y_coordinate]
                        current_square.update_color(color)

    def verify_board_limits(self, i, j):
        if((i < 5 and i >= 0) and (j < 10 and j >= 0)):
            return True
        else:
            return False

    def set_first_square(self, event):
        if (not self.movement_enabler):
            square_position = self.get_clicked_square(event)
            if(square_position):
                square = self.game_board.board[square_position[0]][square_position[1]]
                if(square.has_piece()):
                    range_piece = square.get_piece().get_amount_of_moviment()
                    x = square_position[0]
                    y = square_position[1]
                    self.paint_range(x, y, range_piece, GREY)
                    self.movement_enabler = True
                    self.selected_piece = square.get_piece()

                    return square

                else:
                    # Do nothing
                    pass
            else:
                # Do nothing
                pass

    def set_second_square(self, event, square):
        if(self.movement_enabler):
            new_square_pos = self.get_clicked_square(event)
            if(new_square_pos):
                new_square = self.game_board.board[new_square_pos[0]][new_square_pos[1]]
                if(not new_square.has_piece()):
                    movement = self.calculate_range(square.get_x_board_position(),
                                                    new_square.get_x_board_position(),
                                                    square.get_y_board_position(),
                                                    new_square.get_y_board_position())

                    piece_range = self.selected_piece.get_amount_of_moviment()

                    if(movement <= piece_range):
                        new_square.add_piece(self.selected_piece)
                        self.movement_enabler = False
                        self.selected_piece = None
                        square.remove_piece()
                        self.paint_range(square.get_x_board_position(),
                                         square.get_y_board_position(),
                                         piece_range, WHITE)
                else:
                    # Do nothing
                    pass
            else:
                # Do nothing
                pass

    # Display piece in the correct position after movement
    def draw(self, screen, groups):
        logging.debug("Beginning Move Piece scene's draw method")

        self.game_board.draw(screen)
        self.piece.draw(screen, groups)
        self.piece2.draw(screen, groups)

        logging.debug("Finishing Move Piece scene's draw method")
