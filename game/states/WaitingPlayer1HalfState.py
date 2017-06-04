import logging
from game.states.ArmyPositioningState import *
from game.pieces.DraggablePiece import *

# Messages to guide player turn
TURN_MESSAGE = "Player 1: Select five pieces"

# Number of max pieces to position in this state
PLAYER_1_MAX_PIECES = 2

# Defining a state's state to control state change
RUNNING = False
COMPLETE = True

"""This is the first state to be executed, player 1 will position half of his pieces
to make it fair stategically speaking, the next state should be Player2's turn"""


class WaitingPlayer1HalfState(ArmyPositioningState):

    # The super must be called to build default parent attributes
    def __init__(self, player1_piece_list, player2_piece_list):
        logging.info("Creating player 1 state to choose half of the pieces")
        super().__init__(player1_piece_list, player2_piece_list)

        # Each state has a unique message, indicanting player turn
        self.state_message = TURN_MESSAGE

        logging.info("Player 1 half state created sucessfully")

    # Here, only player 1 pieces are updated, until he chooses half of the max pieces
    def update_player_list(self, events):
        logging.debug("Updated the Left list")
        self.player1_piece_list.update(events)


    # In this state player 1 must position half of the max pieces
    def check_player_turn_requirements(self):
        # Number of pieces player one has positioned this frame.
        number_of_pieces = self.player1_piece_list.count_pieces_in_board()
        if(number_of_pieces >= PLAYER_1_MAX_PIECES):
            return True
        else:
            return False
