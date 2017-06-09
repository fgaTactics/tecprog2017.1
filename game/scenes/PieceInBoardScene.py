import logging
import pygame
from gameEngine.Scene import *
from gameEngine.Mouse import *
from game.gameboard.GameBoard import *
from game.pieces.Engineer import *
from game.pieces.FreshMan import *
from game.pieces.Teacher import *
from game.ArmyService import *
from game.gameboard.PieceMenu import *
from game.PlayerService import *
from gameEngine.GameText import *
from game.gameboard.PieceMenu import *

"""This class show the pieces in the board"""

# Constants to define board's width and height
BOARD_WIDTH = 60
BOARD_HEIGHT = 60
COLOR_BLACK = (0, 0, 0)

# Piece menu positioning in pixels
PLAYER_1_MENU_POSITION = 50
PLAYER_2_MENU_POSITION = 1000
CHANGE_TURN_BUTTON_Y = 475
CHANGE_TURN_BUTTON_WIDTH = 150
CHANGE_TURN_BUTTON_HEIGHT = 100

CHANGE_TURN_BUTTON_FILENAME = "start_button.png"

# Constants to define player's turn
TEXT_PLAYER_TURN_X = 500
TEXT_PLAYER_TURN_Y = 100
PLAYER_ONE = 1
PLAYER_TWO = 2


class PieceInBoardScene(Scene):

    def __init__(self, name="DEFAULT", ID=0):
        super().__init__(name, ID)
        self.player_turn = PLAYER_ONE
        self.game_board = GameBoard(BOARD_HEIGHT)
        self.pieces_in_the_board = []

        self.piece_menu = PieceMenu()

        self.movement_enabler = False
        self.selected_piece = None
        self.previous_square = None

        self.change_turn_button = GameObject(PLAYER_1_MENU_POSITION,
                                             CHANGE_TURN_BUTTON_Y,
                                             CHANGE_TURN_BUTTON_WIDTH,
                                             CHANGE_TURN_BUTTON_HEIGHT,
                                             CHANGE_TURN_BUTTON_FILENAME)

    def load(self):
        logging.info("Load PieceInBoardScene")
        both_player_pieces = ArmyService.get_players_piece_list()
        self.player1_army = both_player_pieces[0]
        self.player2_army = both_player_pieces[1]
        self.pieces_in_the_board.append(self.player1_army)
        self.pieces_in_the_board.append(self.player2_army)

    def draw(self, screen, groups):
        # Fill the screen with black to erase outdated screen
        screen.fill((0, 0, 0))
        logging.info("Drawning table on board")
        self.game_board.draw(screen)
        groups.add(self.change_turn_button.sprite)

        logging.info("Drawning pieces on board")
        for player_pieces in self.pieces_in_the_board:
            for piece in player_pieces:
                piece.draw(screen, groups)

        self.piece_menu.draw(screen, groups)
        self.show_player_turn(self.player_turn)

    # to do how get action for manager turns
    def update(self, events):
        mouse = Mouse()

        # Menu opening
        if(self.player_turn == PLAYER_ONE):
            for piece_player_1 in self.player1_army:
                piece_player_1.update(events)
        else:
            for piece_player_2 in self.player2_army:
                piece_player_2.update(events)

        # Piece movement logic
        if(self.selected_piece is not None):
            if(self.selected_piece.get_player() == self.player_turn):
                self.set_second_square(events, self.previous_square)
            else:
                # Nothing to do
                pass
        else:
            self.previous_square = self.set_first_square(events)

        mouse = Mouse()

        if(mouse.is_mouse_click(self.piece_menu.movement_button, events)):
            if(self.selected_piece is not None):
                if(self.selected_piece.get_player() == self.player_turn):
                    range_piece = self.selected_piece.get_amount_of_moviment()
                    x = self.selected_piece.get_square().get_x_board_position()
                    y = self.selected_piece.get_square().get_y_board_position()
                    self.paint_range(x, y, range_piece, GREY)
                    self.movement_enabler = True
                else:
                    # Nothing to do
                    pass
            else:
                # Nothing to do
                pass
        else:
            # Nothing to do
            pass

        if(mouse.is_mouse_click(self.piece_menu.cancel_button, events)):
            square = self.selected_piece.get_square()
            self.paint_range(square.get_x_board_position(),
                             square.get_y_board_position(),
                             self.selected_piece.get_amount_of_moviment(), WHITE)
            self.selected_piece = None
            self.movement_enabler = False

            self.piece_menu.close()
        else:
            # Nothing to do
            pass

        if(self.selected_piece is not None):
            self.selected_piece.get_square().update_color(GREY)
        else:
            # Nothing to do
            pass

        self.piece_menu.update(events)
        self.manage_player_turn(events)


    def show_player_turn(self, player_number):
        assert player_number > 0 and player_number < 3, "out range for number player"

        if(player_number == PLAYER_ONE):
            GameText.print("Player 1 turn", TEXT_PLAYER_TURN_X,
                           TEXT_PLAYER_TURN_Y)
            logging.info("Player1 turn")
        else:
            GameText.print("Player 2 turn", TEXT_PLAYER_TURN_X,
                           TEXT_PLAYER_TURN_Y)
            logging.info("Player2 turn")

    # Use the time turn while actions piece is not ready
    def manage_player_turn(self, events):

        mouse = Mouse()
        if(mouse.is_mouse_click(self.change_turn_button, events)):
            logging.info("Player clicked to change turn")

            # Close all open menus
            self.piece_menu.close()

            if(self.player_turn == PLAYER_ONE):
                logging.info("Change to player two turn")
                self.change_turn_button.set_x(PLAYER_2_MENU_POSITION)
                self.piece_menu.set_positions(PLAYER_2_MENU_POSITION)
                self.player_turn = PLAYER_TWO
            else:
                logging.info("Change to player one turn")
                self.change_turn_button.set_x(PLAYER_1_MENU_POSITION)
                self.piece_menu.set_positions(PLAYER_1_MENU_POSITION)
                self.player_turn = PLAYER_ONE
        else:
            # nothing to do
            pass

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
        """ The loops contain a plus one addition aiming the case that x_coordinate
        is equal to given statement """
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

    def verify_board_limits(self, x_coordinate, y_coordinate):
        # The board cannot have negative coordinates
        if((x_coordinate < self.game_board.amount_of_rows and x_coordinate >= 0) and
           (y_coordinate < self.game_board.amount_of_columns and y_coordinate >= 0)):
            return True
        else:
            return False

    def set_first_square(self, event):
        if (not self.movement_enabler):
            square_position = self.get_clicked_square(event)
            if(square_position is not None):
                square = self.game_board.board[square_position[0]][square_position[1]]
                if(square.has_piece()):
                    self.selected_piece = square.get_piece()
                    return square
                else:
                    # Do nothing
                    pass
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
                        self.piece_menu.close()
                else:
                    # Do nothing
                    pass
            else:
                # Do nothing
                pass
