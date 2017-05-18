import logging
from game.states.ArmyPositioningState import *
from game.pieces.DraggablePiece import *


# Messages to guide player turns
TURN_MESSAGE = "Player 1: Select your remaining pieces"

# Number of pieces to position each turn
PLAYER_1_PIECES_SECOND_TURN = 10

RUNNING = False
COMPLETE = True


class WaitingPlayer1CompleteState(ArmyPositioningState):

    def __init__(self, player1_piece_list, player2_piece_list):
        super().__init__(player1_piece_list, player2_piece_list)
        self.state_message = TURN_MESSAGE


    def update_player_list(self, events):
        logging.debug("Updated the Left list")
        self.player1_piece_list.update(events)

    def show_confirm_button(self, screen, groups):
        if(self.player1_piece_list.count_pieces_in_board() >=
           PLAYER_1_PIECES_SECOND_TURN):
            logging.debug("Player 1 can confirm again")
            groups.add(self.confirm_button.sprite)

    def verify_player_confirmation(self, events):
        if(self.player1_piece_list.count_pieces_in_board() >=
           PLAYER_1_PIECES_SECOND_TURN):
            DraggablePiece.set_drag_enable(False)
            logging.debug("Player 1 can confirm again")

            self.verify_mouse_click_on_confirm(events)
        # Player can't click confirm, dragging new pieces is valid
        else:
            logging.info("The player can't confirm")
            DraggablePiece.set_drag_enable(True)
