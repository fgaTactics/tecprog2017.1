import logging
from gameEngine.GameEngine import *
from gameEngine.Scene import *
from game.gameboard.GameBoard import *
from game.gameboard.PieceList import *
from game.PlayerService import *
from gameEngine.Mouse import *
from gameEngine.SceneManager import *

# Square size in pixels
GAME_BOARD_SQUARE_SIZE = 60

# Confirmation button positioning in pixels
CONFIRM_BUTTON_X = 500
CONFIRM_BUTTON_Y = 150
CONFIRM_BUTTON_WIDTH = 150
CONFIRM_BUTTON_HEIGHT = 150

CONFIRM_BUTTON_FILENAME = "start_button.png"

# Players Piece lists positioning values and size, both in pixels
LEFT_LIST_X = 0
LEFT_LIST_Y = 0
RIGHT_LIST_X = 1000
RIGHT_LIST_Y = 0

PIECE_LIST_WIDTH = 200
PIECE_LIST_HEIGHT = 800

PIECE_LIST_BACKGROUND_FILENAME = "PieceMenu.jpg"

# Player Turn text indicator position in pixels
PLAYER_TURN_MESSAGE_X = 400
PLAYER_TURN_MESSAGE_Y = 100

# Messages to guide player turns
TURN_MESSAGE_1 = "Player 1: Select five pieces"
TURN_MESSAGE_2 = "Player 2: Select your pieces"
TURN_MESSAGE_3 = "Player 1: Select your remaining pieces"

# Number of pieces to position each turn
PLAYER_1_PIECES_FIRST_TURN = 5
PLAYER_2_PIECES_FIRST_TURN = 10
PLAYER_1_PIECES_SECOND_TURN = 10

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

        # Flags to manage player turns in positioning as the game defines
        self.player1_first_confirm = False
        self.player1_second_confirm = False
        self.player2_confirm = False

        # We use the same confirm button to check all the confirmations
        self.confirm_button = GameObject(CONFIRM_BUTTON_X, CONFIRM_BUTTON_Y,
                                         CONFIRM_BUTTON_WIDTH, CONFIRM_BUTTON_HEIGHT,
                                         CONFIRM_BUTTON_FILENAME)

        logging.info("Army positioning scene ready")


    # Initialize available piece lists based on player classes from ClassSelectionScene.
    def load(self):
        logging.info("Loading Army Positioning Scene")

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

        # Print the confirm button if conditions are met
        self.show_confirm_button(screen, groups)

        # Print a message indicating which player turn it is
        self.show_player_turn_message()

        logging.debug("Army Positioning Draw end")


    # Based on the turn confirmation, show a message indicating which player turn is
    def show_player_turn_message(self):
        logging.debug("Printing turn message")
        if(self.player1_first_confirm is False):
            logging.debug("It's  player 1 turn")
            GameText.print(TURN_MESSAGE_1, PLAYER_TURN_MESSAGE_X, PLAYER_TURN_MESSAGE_Y)
        elif(self.player2_confirm is False):
            logging.debug("It's player 2 turn")
            GameText.print(TURN_MESSAGE_2, PLAYER_TURN_MESSAGE_X, PLAYER_TURN_MESSAGE_Y)
        elif(self.player2_confirm is True):
            logging.debug("It's player 1 turn again")
            GameText.print(TURN_MESSAGE_3, PLAYER_TURN_MESSAGE_X, PLAYER_TURN_MESSAGE_Y)


    # The confirm button must only be shown if the player has enough pieces on the board
    def show_confirm_button(self, screen, groups):
        logging.debug("Checking if confirm button is necessary")

        if(self.player1_first_confirm is False and
           self.left_piece_list.count_pieces_in_board() >= PLAYER_1_PIECES_FIRST_TURN):
            logging.debug("Player 1 can first confirm")
            groups.add(self.confirm_button.sprite)

        elif(self.player2_confirm is False and
             self.right_piece_list.count_pieces_in_board() >= PLAYER_2_PIECES_FIRST_TURN):
            logging.debug("Player 2 can confirm")
            groups.add(self.confirm_button.sprite)

        elif(self.player1_second_confirm is False and
             self.left_piece_list.count_pieces_in_board() >= PLAYER_1_PIECES_SECOND_TURN):
            logging.debug("Player 1 can confirm again")
            groups.add(self.confirm_button.sprite)

        # If none of the players can confirm, the button is disabled
        else:
            self.confirm_button_is_visible = False

        logging.debug("Confirm button checking complete")


    # We must only update the list of the player that the turn belongs to
    def update(self, events):
        logging.debug("Army positioning update start")

        # To prevent a player playing in the wrong turn, only one list must be updated
        logging.debug("Verifying which piece list to update")
        if(self.player1_first_confirm is False):
            logging.debug("Updated the Left list")
            self.left_piece_list.update(events)

        elif(self.player2_confirm is False):
            logging.debug("Updated the Right list")
            self.right_piece_list.update(events)

        elif(self.player2_confirm is True):
            logging.debug("Updated the Left list")
            self.left_piece_list.update(events)

        # Verify player confirmations to change turns
        self.verify_player_confirmation(events)

        logging.debug("Army positioning Scene Update done")


    # Checks if the player can end his turn
    def verify_player_confirmation(self, events):
        logging.debug("Checking if any player can click confirm")
        mouse = Mouse()

        # Verify the end of the first player, first turn
        if(self.player1_first_confirm is False and
           self.left_piece_list.count_pieces_in_board() >= PLAYER_1_PIECES_FIRST_TURN):
            DraggablePiece.set_drag_enable(False)
            logging.debug("Player 1 can first confirm")

            if(mouse.is_mouse_click(self.confirm_button, events)):
                logging.info("Player 1 clicked confirm")
                self.player1_first_confirm = True

        # Verify the end of the second player turn
        elif(self.player2_confirm is False and
             self.right_piece_list.count_pieces_in_board() >= PLAYER_2_PIECES_FIRST_TURN):
            DraggablePiece.set_drag_enable(False)
            logging.debug("Player 2 can confirm")

            if(mouse.is_mouse_click(self.confirm_button, events)):
                logging.info("Player 2 clicked confirm")
                self.player2_confirm = True

        # Verify the end of the first player turn
        elif(self.player1_second_confirm is False and
             self.left_piece_list.count_pieces_in_board() >= PLAYER_1_PIECES_SECOND_TURN):
            DraggablePiece.set_drag_enable(False)
            logging.debug("Player 1 can confirm again")

            # if confirmed here, all pieces are ready, game can begin
            if(mouse.is_mouse_click(self.confirm_button, events)):
                self.player1_second_confirm = False
                logging.info("Player 1 clicked confirm")
                logging.info("Game Start")
                gameEngine = GameEngine.get_instance()
                gameEngine.scene_manager.load_next_scene()

        # None of the players can click confirm, dragging new pieces is valid
        else:
            logging.info("Nobody can click confirm")
            DraggablePiece.set_drag_enable(True)

        logging.debug("End of confirm checking")
