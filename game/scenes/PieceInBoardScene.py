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
from gameEngine.GameMusic import *
"""This class show the pieces in the board"""

# Constants to define board's width and height
BOARD_WIDTH = 60
BOARD_HEIGHT = 60

COLOR_BLACK = (0, 0, 0)
RED = (255, 0, 0)

# Piece menu positioning in pixels
PLAYER_1_MENU_POSITION = 50
PLAYER_2_MENU_POSITION = 1000

# Change turn button positioning in pixels
CHANGE_TURN_BUTTON_Y = 475
CHANGE_TURN_BUTTON_WIDTH = 150
CHANGE_TURN_BUTTON_HEIGHT = 100

CHANGE_TURN_BUTTON_FILENAME = "start_button.png"

# Constants to define player's turn
TEXT_PLAYER_TURN_X = 500
TEXT_PLAYER_TURN_Y = 100
PLAYER_ONE = 1
PLAYER_TWO = 2

# Adding constant to music name
MUSIC_NAME = "battle.mp3"


class PieceInBoardScene(Scene):

    def __init__(self, name="DEFAULT", ID=0):
        super().__init__(name, ID)
        self.player_turn = PLAYER_ONE
        self.game_board = GameBoard(BOARD_HEIGHT)
        self.pieces_in_the_board = []

        self.piece_menu = PieceMenu()

        self.movement_enabler = False
        self.attack_enabler = False

        self.selected_piece = None
        # Load music on scene
        self.game_scene_music = GameMusic(MUSIC_NAME)

        # Load music on scene
        self.game_scene_music = GameMusic(MUSIC_NAME)

        self.change_turn_button = GameObject(PLAYER_1_MENU_POSITION,
                                             CHANGE_TURN_BUTTON_Y,
                                             CHANGE_TURN_BUTTON_WIDTH,
                                             CHANGE_TURN_BUTTON_HEIGHT,
                                             CHANGE_TURN_BUTTON_FILENAME)

    def load(self):
        logging.info("Load PieceInBoardScene")

        self.game_scene_music.play_music()

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
        self.action_done = False
        if((self.selected_piece is not None) and
           (self.selected_piece.get_player() == self.player_turn)):
            # Enable movement by Piece Menu's movement button
            self.menu_move_action(events)
            self.menu_attack_action(events)

            # Piece movement logic
            self.move_piece_to(events)
            self.attack_piece(events)

            # Cancel any piece action
            self.menu_cancel_action(events)
        else:
            self.get_clicked_piece(events)

            # Menu opening
            self.open_menu(events)

        # Highlight selected piece on board
        self.highlight_selected_piece()

        self.piece_menu.update(events)
        self.manage_player_turn(events)
        self.remove_dead_pieces(self.player1_army)
        self.remove_dead_pieces(self.player2_army)
        self.verify_win_or_lose()

    def verify_win_or_lose(self):
        if(len(self.player1_army) <= 0):
            GameText.print("PLAYER 1 PERDEU", 450, 300)
        elif(len(self.player2_army) <= 0):
            GameText.print("PLAYER 2 PERDEU", 450, 300)

    # Moves selected piece to a certain square
    def move_piece_to(self, events):
        if(self.movement_enabler and
           self.selected_piece.get_player() == self.player_turn):
            self.get_move_target_square(events)
        else:
            # Nothing to do
            pass

    def attack_piece(self, events):
        if(self.attack_enabler and self.selected_piece.get_player() == self.player_turn):
            self.get_attack_target_square(events)
        else:
            # Nothing to do
            pass

    # Action triggered by the "Move" menu button
    def menu_move_action(self, events):
        mouse = Mouse()
        if(mouse.is_mouse_click(self.piece_menu.movement_button, events)):
            self.enable_movement()
        else:
            # Nothing to do
            pass

    # Action triggered by the "Attack" menu button
    def menu_attack_action(self, events):
        mouse = Mouse()
        if(mouse.is_mouse_click(self.piece_menu.attack_button, events)):
            self.enable_attack()
        else:
            # Nothing to do
            pass

    # Action triggered by the "Cancel" menu button
    def menu_cancel_action(self, events):
        mouse = Mouse()
        if(mouse.is_mouse_click(self.piece_menu.cancel_button, events)):
            self.deselect_piece()
        else:
            # Nothing to do
            pass


    # Allows a player to move one of his pieces
    def enable_movement(self):
        if(self.selected_piece.get_player() == self.player_turn):
            piece_range = self.selected_piece.get_amount_of_moviment()
            piece_square = self.selected_piece.get_square()
            self.reset_painted_range()
            self.paint_range(piece_square.get_x_board_position(),
                             piece_square.get_y_board_position(),
                             piece_range, GREY)
            self.movement_enabler = True
            self.attack_enabler = False
        else:
            # Nothing to do
            pass

    def enable_attack(self):
        if(self.selected_piece.get_player() == self.player_turn):
            piece_range = self.selected_piece.get_range()
            piece_square = self.selected_piece.get_square()
            self.reset_painted_range()
            self.paint_range(piece_square.get_x_board_position(),
                             piece_square.get_y_board_position(),
                             piece_range, RED)
            self.attack_enabler = True
            self.movement_enabler = False
        else:
            # Nothing to do
            pass

    # Open the menu when a piece is clicked
    def open_menu(self, events):
        if(self.player_turn == PLAYER_ONE):
            for piece_player_1 in self.player1_army:
                piece_player_1.update(events)
        else:
            for piece_player_2 in self.player2_army:
                piece_player_2.update(events)


    def highlight_selected_piece(self):
        if(self.selected_piece is not None):
            if(self.selected_piece.get_player() == self.player_turn):
                self.selected_piece.get_square().update_color(GREY)
            else:
                # Nothing to do
                pass
        else:
            # Nothing to do
            pass


    def deselect_piece(self):
        self.reset_painted_range()
        self.selected_piece = None
        self.movement_enabler = False
        self.attack_enabler = False
        self.piece_menu.close()

    def reset_painted_range(self):
        max_range = 100
        square = self.selected_piece.get_square()
        self.paint_range(square.get_x_board_position(),
                         square.get_y_board_position(),
                         max_range, WHITE)

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


    # Switch between player turns
    def manage_player_turn(self, events):
        mouse = Mouse()
        if(self.action_done):
            logging.info("Player realized an action")

            if(self.selected_piece is not None):
                self.deselect_piece()
            else:
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


    # Return the square clicked by the player
    def get_clicked_square(self, events):
        for row in range(self.game_board.amount_of_rows):
            for column in range(self.game_board.amount_of_columns):
                square = self.game_board.board[row][column]
                rectangle = pygame.Rect(square.initial_x_position,
                                        square.initial_y_position,
                                        square.get_width(),
                                        square.get_height())

                if(events.type == pygame.MOUSEBUTTONUP):
                    mouse_position = pygame.mouse.get_pos()

                    if(rectangle.collidepoint(mouse_position[0], mouse_position[1])):
                        return (row, column)
                    else:
                        # nothing to do
                        pass
                else:
                    # nothing to do
                    pass


    # Calculate which squares are within the piece's range
    def calculate_range(self, x_piece_coordinate, x_coordinate,
                        y_piece_coordinate, y_coordinate):
        piece_range = (abs(x_piece_coordinate - x_coordinate) +
                       abs(y_piece_coordinate - y_coordinate))

        return piece_range


    # Change the color of squares within the piece's range
    def paint_range(self, x_piece_coordinate, y_piece_coordinate, piece_range, color):
        """ The loops contain a plus one addition aiming the case when x_coordinate
        is equal to given statement """
        for x_coordinate in range(x_piece_coordinate - piece_range,
                                  x_piece_coordinate + piece_range + 1):
            for y_coordinate in range(y_piece_coordinate - piece_range,
                                      y_piece_coordinate + piece_range + 1):

                # Calculate the piece's reach
                movement = self.calculate_range(x_piece_coordinate, x_coordinate,
                                                y_piece_coordinate, y_coordinate)
                if(movement <= piece_range):
                    if(self.verify_board_limits(x_coordinate, y_coordinate)):
                        current_square = self.game_board.board[x_coordinate][y_coordinate]
                        current_square.update_color(color)


    # Check if the clicked square is inside the board
    def verify_board_limits(self, x_coordinate, y_coordinate):
        # The board cannot have negative coordinates
        if((x_coordinate < self.game_board.amount_of_rows and x_coordinate >= 0) and
           (y_coordinate < self.game_board.amount_of_columns and y_coordinate >= 0)):
            return True
        else:
            return False

    # Return the piece clicked by the player
    def get_clicked_piece(self, events):
        if (not self.movement_enabler):
            square_position = self.get_clicked_square(events)
            if(square_position is not None):
                square = self.game_board.board[square_position[0]][square_position[1]]
                if(square.has_piece()):
                    self.selected_piece = square.get_piece()
                else:
                    # Do nothing
                    pass
            else:
                # Do nothing
                pass
        else:
            # Do nothing
            pass


    def get_move_target_square(self, events):
        if(self.movement_enabler):
            new_square_pos = self.get_clicked_square(events)
            if(new_square_pos):
                new_square = self.game_board.board[new_square_pos[0]][new_square_pos[1]]
                if(not new_square.has_piece()):
                    current_square = self.selected_piece.get_square()
                    movement = self.calculate_range(current_square.get_x_board_position(),
                                                    new_square.get_x_board_position(),
                                                    current_square.get_y_board_position(),
                                                    new_square.get_y_board_position())

                    piece_range = self.selected_piece.get_amount_of_moviment()
                    self.move_in_range(piece_range, movement, new_square, current_square)
                else:
                    # Do nothing
                    pass
            else:
                # Do nothing
                pass
        else:
            # Do nothing
            pass

    def get_attack_target_square(self, events):
        if(self.attack_enabler):
            new_square_pos = self.get_clicked_square(events)
            if(new_square_pos):
                new_square = self.game_board.board[new_square_pos[0]][new_square_pos[1]]
                if(new_square.has_piece()):
                    target_piece = new_square.get_piece()
                    if(target_piece.get_player() is not self.player_turn):
                        current_square = self.selected_piece.get_square()
                        rng = self.calculate_range(current_square.get_x_board_position(),
                                                   new_square.get_x_board_position(),
                                                   current_square.get_y_board_position(),
                                                   new_square.get_y_board_position())
                        self.attack(self.selected_piece, target_piece, rng)
                    else:
                        # Do nothing
                        pass
                else:
                    # Do nothing
                    pass
            else:
                # Do nothing
                pass
        else:
            # Do nothing
            pass


    # Check if the target square is within the range of the part
    def move_in_range(self, piece_range, movement, new_square, current_square):
        if(movement <= piece_range):
            self.paint_range(current_square.get_x_board_position(),
                             current_square.get_y_board_position(),
                             piece_range, WHITE)

            new_square.add_piece(self.selected_piece)
            current_square.remove_piece()
            self.movement_enabler = False
            self.selected_piece = None
            self.piece_menu.close()
            self.action_done = True
        else:
            # Do nothing
            pass

    def attack(self, piece, attacked_piece, attack_distance):
        if(attack_distance <= piece.get_range()):
            self.paint_range(piece.get_square().get_x_board_position(),
                             piece.get_square().get_y_board_position(),
                             piece.get_range(), WHITE)
            attacked_piece.take_damage(piece.get_attack())
            self.attack_enabler = False
            self.selected_piece = None
            self.piece_menu.close()
            self.action_done = True
        else:
            # Do nothing
            pass

    def remove_dead_pieces(self, player_army):
        for piece in player_army:
            if(piece.is_dead()):
                piece_square = piece.get_square()
                piece_square.remove_piece()
                player_army.remove(piece)
            else:
                # Do nothing
                pass
