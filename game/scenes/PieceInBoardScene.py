import logging
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

# Change turn button positioning in pixels
CHANGE_TURN_BUTTON_X = 200
CHANGE_TURN_BUTTON_Y = 50
CHANGE_TURN_BUTTON_WIDTH = 150
CHANGE_TURN_BUTTON_HEIGHT = 150

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

        self.change_turn_button = GameObject(CHANGE_TURN_BUTTON_X,
                                             CHANGE_TURN_BUTTON_Y,
                                             CHANGE_TURN_BUTTON_WIDTH,
                                             CHANGE_TURN_BUTTON_HEIGHT,
                                             CHANGE_TURN_BUTTON_FILENAME)

    def load(self):
        ###           MOCK          ###
        ###############################
        player1_list = []
        player2_list = []

        x = self.game_board.board[0][0].get_x_position()
        y = self.game_board.board[0][0].get_y_position()
        piece = DraggablePiece(x,y, 50, 50, "pieces/engineer.jpg", "engineer")
        player1_list.append(piece)
        self.game_board.board[0][0].add_piece(piece)
        
        x = self.game_board.board[0][1].get_x_position()
        y = self.game_board.board[0][1].get_y_position()
        piece = DraggablePiece(x,y, 50, 50, "pieces/engineer.jpg", "engineer")
        player2_list.append(piece)
        self.game_board.board[0][1].add_piece(piece)

        ArmyService.set_piece_list(player1_list)
        ArmyService.set_piece_list(player2_list)
        ###############################


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

        if(self.player_turn == PLAYER_ONE):
            for piece_player_1 in self.player1_army:
                piece_player_1.update(events)
        else:
            for piece_player_2 in self.player2_army:
                piece_player_2.update(events)

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
                self.player_turn = PLAYER_TWO
            else:
                logging.info("Change to player one turn")
                self.player_turn = PLAYER_ONE
        else:
            # nothing to do
            pass
