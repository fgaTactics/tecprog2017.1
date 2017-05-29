import logging

from gameEngine.Scene import *
from game.gameboard.GameBoard import *
from game.gameboard.PieceList import *
from game.PlayerService import *
from gameEngine.SceneManager import *
from game.ArmyService import *
from gameEngine.GameEngine import *
from game.states.WaitingPlayer1HalfState import *
from game.states.WaitingPlayer1CompleteState import *
from game.states.WaitingPlayer2State import *
from gameEngine.GameMusic import *

# Square size in pixels
GAME_BOARD_SQUARE_SIZE = 60

# Players Piece lists positioning values and size, both in pixels
LEFT_LIST_X = 0
LEFT_LIST_Y = 0
RIGHT_LIST_X = 1000
RIGHT_LIST_Y = 0

PLAYER_1 = 1
PLAYER_2 = 2

PIECE_LIST_WIDTH = 200
PIECE_LIST_HEIGHT = 800

PIECE_LIST_BACKGROUND_FILENAME = "PieceMenu.jpg"

# Add constant to music name
MUSIC_NAME = "selection.mp3"

""" The Army Positioning Scene is where the players will choose their soldiers to battle.
Players take turns on piece positioning, being 5 pieces to player 1, then 10 to player 2,
then the remaining 5 to player 1.
Players must confirm their choices each turn to complete the action. """


class ArmyPositioningScene(Scene):

    # Initialize player choices, create the gameboard and confirmation button
    def __init__(self, name="DEFAULT", ID=0):
        logging.info("Constructing Army Positioning Scene")
        super().__init__(name, ID)

        # Game Board to hold the pieces for both players
        self.game_board = GameBoard(GAME_BOARD_SQUARE_SIZE)

        # Load music on scene
        self.positioning_scene_music = GameMusic(MUSIC_NAME)

        logging.info("Army positioning scene ready")


    # Initialize available piece lists based on player classes from ClassSelectionScene.
    def load(self):
        logging.info("Loading Army Positioning Scene")

        self.positioning_scene_music.play_music()

        # Player service saves classes on an array in order.
        logging.info("Loading Player classes")
        player1_class = PlayerService.get_player(0)
        player2_class = PlayerService.get_player(1)

        # Create piece lists for both players based on their chosen classes
        logging.info("Creating Piece lists")
        self.left_piece_list = PieceList(player1_class, LEFT_LIST_X, LEFT_LIST_Y,
                                         PIECE_LIST_WIDTH, PIECE_LIST_HEIGHT,
                                         PIECE_LIST_BACKGROUND_FILENAME)
        self.right_piece_list = PieceList(player2_class, RIGHT_LIST_X, RIGHT_LIST_Y,
                                          PIECE_LIST_WIDTH, PIECE_LIST_HEIGHT,
                                          PIECE_LIST_BACKGROUND_FILENAME)

        states = []
        states.append(WaitingPlayer1HalfState(self.left_piece_list,
                                              self.right_piece_list))
        states.append(WaitingPlayer2State(self.left_piece_list,
                                          self.right_piece_list))
        states.append(WaitingPlayer1CompleteState(self.left_piece_list,
                                                  self.right_piece_list))

        self.states = iter(states)
        self.current_state = next(self.states)

        logging.info("Loading Army Positioning done")


    # Draw the board, both player lists and informative texts based on confirmations
    def draw(self, screen, groups):
        logging.debug("ArmyPositioning Draw start:")

        # Print a black background to erase the screen
        screen.fill((0, 0, 0))

        # Print piece lists and gameboard on the screen
        self.game_board.draw(screen)
        self.left_piece_list.draw(screen, groups)
        self.right_piece_list.draw(screen, groups)

        self.current_state.draw(screen, groups)

        logging.debug("Army Positioning Draw end")

    # We must only update the list of the player that the turn belongs to
    def update(self, events):
        self.current_state.update(events)
        self.verify_change_in_state()

    def verify_change_in_state(self):
        if(self.current_state.is_done()):
            try:
                self.current_state = next(self.states)
            except:
                logging.info("Saving armies")
                self.save_army()
                self.change_scene()
        else:
            # Do Nothing
            pass

    def save_army(self):
        player1_army = []
        player2_army = []
        army_list = []

        army_list = self.left_piece_list.get_pieces_on_board()
        for piece in army_list:
            piece.set_player(PLAYER_1)
            player1_army.append(piece)

        army_list = self.right_piece_list.get_pieces_on_board()
        for piece in army_list:
            piece.set_player(PLAYER_2)
            player2_army.append(piece)

        ArmyService.set_piece_list(player1_army)
        ArmyService.set_piece_list(player2_army)

    def change_scene(self):
        logging.info("Changing scene")
        game_engine = GameEngine.get_instance()
        game_engine.scene_manager.load_next_scene()
