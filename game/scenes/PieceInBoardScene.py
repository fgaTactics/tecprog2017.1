import logging
from gameEngine.Scene import *
from gameEngine.Mouse import *
from gameEngine.GameEngine import *
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

# Restart match button positions in pixel
RESTART_MATCH_BUTTON_X = 400
RESTART_MATCH_BUTTON_Y = 50
RESTART_MATCH_BUTTON_WIDTH = 150
RESTART_MATCH_BUTTON_HEIGHT = 150

# Restart game button positions in pixel
RESTART_GAME_BUTTON_X = 400
RESTART_GAME_BUTTON_Y = 200
RESTART_GAME_BUTTON_WIDTH = 150
RESTART_GAME_BUTTON_HEIGHT = 150

# Restart positioning button positions in pixel
RESTART_POSITIONING_BUTTON_X = 400
RESTART_POSITIONING_BUTTON_Y = 350
RESTART_POSITIONING_BUTTON_WIDTH = 150
RESTART_POSITIONING_BUTTON_HEIGHT = 150

CHANGE_TURN_BUTTON_FILENAME = "start_button.png"
RESTART_MATCH_BUTTON_FILENAME = "start_button.png"
RESTART_GAME_BUTTON_FILENAME = "start_button.png"
RESTART_POSITIONING_BUTTON_FILENAME = "start_button.png"

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
        logging.info("Load PieceInBoardScene")
        both_player_pieces = ArmyService.get_players_piece_list()
        self.player1_army = both_player_pieces[0]
        self.player2_army = both_player_pieces[1]
        self.pieces_in_the_board.append(self.player1_army)
        self.pieces_in_the_board.append(self.player2_army)
        self.gameOver = False


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

        if(self.gameOver):
            self.__create_restart_buttons()
            self.__show_restart_options(screen, groups)
        else:
            # Do nothing
            pass


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

        if(self.gameOver):
            self.__create_restart_buttons()
            self.__verify_restart_option(events)

        # Emulate victory condition
        if(events.type == pygame.KEYDOWN):
            self.gameOver = True



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


    # Verify if the players chosen restart game or restart match
    def __verify_restart_option(self, event):
        mouse = Mouse()
        if(mouse.is_mouse_click(self.restart_match_button, event)):
            self.__restart_match()
            logging.info("Restart match")
        elif(mouse.is_mouse_click(self.restart_game_button, event)):
            self.__restart_game()
            logging.info("Restart game")
        elif(mouse.is_mouse_click(self.restart_positioning_button, event)):
            self.__restart_position()
            logging.info("Restart to army position")


    # Show final match menu
    def __show_restart_options(self, screen, groups):
        self.restart_match_button.draw(screen, groups)
        self.restart_positioning_button.draw(screen, groups)
        self.restart_game_button.draw(screen, groups)


    # Restart to the start scene to choose another class
    def __restart_game(self):
        gameEngine = GameEngine.get_instance()
        gameEngine.scene_manager.load_scene("Start Menu")


    # Restart the match with same player1 and player2 army
    def __restart_match(self):
        self.load()


    # Restart to the army positioning scene
    def __restart_position(self):
        gameEngine = GameEngine.get_instance()
        gameEngine.scene_manager.load_scene("Army Positioning")


    def __create_restart_buttons(self):
        self.restart_match_button = GameObject(RESTART_MATCH_BUTTON_X,
                                               RESTART_MATCH_BUTTON_Y,
                                               RESTART_MATCH_BUTTON_WIDTH,
                                               RESTART_MATCH_BUTTON_HEIGHT,
                                               RESTART_MATCH_BUTTON_FILENAME)
    
        self.restart_game_button = GameObject(RESTART_GAME_BUTTON_X,
                                              RESTART_GAME_BUTTON_Y,
                                              RESTART_GAME_BUTTON_WIDTH,
                                              RESTART_GAME_BUTTON_HEIGHT,
                                              RESTART_GAME_BUTTON_FILENAME)
    
        self.restart_positioning_button = GameObject(RESTART_POSITIONING_BUTTON_X,
                                                     RESTART_POSITIONING_BUTTON_Y,
                                                     RESTART_POSITIONING_BUTTON_WIDTH,
                                                     RESTART_POSITIONING_BUTTON_HEIGHT,
                                                     RESTART_POSITIONING_BUTTON_FILENAME)
