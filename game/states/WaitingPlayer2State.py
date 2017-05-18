import logging
from game.states.ArmyPositioningState import *
from game.pieces.DraggablePiece import *

TURN_MESSAGE = "Player 2: Select your pieces"

# Number of pieces to position each turn
PLAYER_2_PIECES_FIRST_TURN = 10

RUNNING = False
COMPLETE = True


class WaitingPlayer2State(ArmyPositioningState):

    def __init__(self, player1_piece_list, player2_piece_list):
        super().__init__(player1_piece_list, player2_piece_list)
        self.state_message = TURN_MESSAGE


    def update_player_list(self, events):
        logging.debug("Updated the Right list")
        self.player2_piece_list.update(events)

    def show_confirm_button(self, screen, groups):
        if(self.player2_piece_list.count_pieces_in_board() >= PLAYER_2_PIECES_FIRST_TURN):
            logging.debug("Player 2 can confirm")
            groups.add(self.confirm_button.sprite)

    def verify_player_confirmation(self, events):
        # Verify the end of the second player turn
        if(self.player2_piece_list.count_pieces_in_board() >= PLAYER_2_PIECES_FIRST_TURN):
            DraggablePiece.set_drag_enable(False)
            logging.debug("Player 2 can confirm")

            self.verify_mouse_click_on_confirm(events)
        # Player can't click confirm, dragging new pieces is valid
        else:
            logging.info("The player can't confirm")
            DraggablePiece.set_drag_enable(True)
