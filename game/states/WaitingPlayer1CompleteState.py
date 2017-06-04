import logging
from game.states.ArmyPositioningState import *
from game.pieces.DraggablePiece import *

# Messages to guide player turn
TURN_MESSAGE = "Player 1: Select your remaining pieces"

# Number of max pieces to position in this state
PLAYER_1_MAX_PIECES = 4

# Defining a state's state to control state change
RUNNING = False
COMPLETE = True

"""This state implements the conditions to the second part of the player 1
positioning turn. Having more pieces enabled then the first player 1 state,
and being executed after player2state"""


class WaitingPlayer1CompleteState(ArmyPositioningState):

    # The super must be called to build default parent attributes
    def __init__(self, player1_piece_list, player2_piece_list):
        logging.info("Creating player 1 complete state")
        super().__init__(player1_piece_list, player2_piece_list)

        # Each state has a unique message, indicanting player turn
        self.state_message = TURN_MESSAGE

        logging.info("Player 1 state created sucessfully")

    # In this state, only player 1 pieces are updated, player2 should be already done
    def update_player_list(self, events):
        logging.debug("Updating Player 1 list")
        self.player1_piece_list.update(events)

    # In this state player 1 must position all 10 pieces
    def check_player_turn_requirements(self):
        # Number of pieces player one has positioned this frame.
        number_of_pieces = self.player1_piece_list.count_pieces_in_board()
        if(number_of_pieces >= PLAYER_1_MAX_PIECES):
            return True
        else:
            return False
