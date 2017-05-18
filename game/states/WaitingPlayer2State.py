import logging
from game.states.ArmyPositioningState import *
from game.pieces.DraggablePiece import *

# Messages to guide player turn
TURN_MESSAGE = "Player 2: Select your pieces"

# Number of max pieces to position in this state
PLAYER_2_MAX_PIECES = 10

# Defining a state's state to control state change
RUNNING = False
COMPLETE = True

"""In this state player 2 will position all his pieces in the board, making his
play after player 1 positioned half his pieces in the first state."""


class WaitingPlayer2State(ArmyPositioningState):

    # The super must be called to build default parent attributes
    def __init__(self, player1_piece_list, player2_piece_list):
        logging.info("Creating player 2 state to choose all pieces")
        super().__init__(player1_piece_list, player2_piece_list)

        # Each state has a unique message, indicanting player turn
        self.state_message = TURN_MESSAGE

        logging.info("Player 2 state created sucessfully")


    def update_player_list(self, events):
        logging.debug("Updated the Right list")
        self.player2_piece_list.update(events)

    # In this state player 2 must position all his pieces
    def check_player_turn_requirements(self):
        # Number of pieces player 2 has positioned this frame.
        number_of_pieces = self.player2_piece_list.count_pieces_in_board()
        if(number_of_pieces >= PLAYER_2_MAX_PIECES):
            return True
        else:
            return False
