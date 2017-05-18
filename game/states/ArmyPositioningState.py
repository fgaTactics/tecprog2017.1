import logging
from gameEngine.Mouse import *
from gameEngine.GameObject import *
from gameEngine.GameText import *

# Confirmation button positioning in pixels
CONFIRM_BUTTON_X = 500
CONFIRM_BUTTON_Y = 150
CONFIRM_BUTTON_WIDTH = 150
CONFIRM_BUTTON_HEIGHT = 150

CONFIRM_BUTTON_FILENAME = "start_button.png"

# Player Turn text indicator position in pixels
PLAYER_TURN_MESSAGE_X = 400
PLAYER_TURN_MESSAGE_Y = 100

RUNNING = False
COMPLETE = True


class ArmyPositioningState:


    def __init__(self, player1_piece_list, player2_piece_list):
        self.state = RUNNING
        self.player1_piece_list = player1_piece_list
        self.player2_piece_list = player2_piece_list
        self.state_message = "Default message"
        self.confirm_button = GameObject(CONFIRM_BUTTON_X, CONFIRM_BUTTON_Y,
                                         CONFIRM_BUTTON_WIDTH, CONFIRM_BUTTON_HEIGHT,
                                         CONFIRM_BUTTON_FILENAME)


    def update(self, events):
        self.update_player_list(events)
        self.verify_player_confirmation(events)

    def draw(self, screen, groups):
        # Print the confirm button if conditions are met
        self.show_confirm_button(screen, groups)

        # Print a message indicating which player turn it is
        self.show_player_turn_message()

    def verify_mouse_click_on_confirm(self, events):
        mouse = Mouse()
        if(mouse.is_mouse_click(self.confirm_button, events)):
            logging.warning("Player clicked confirm")
            self.state = COMPLETE
        else:
            # Do nothing
            pass

    def show_player_turn_message(self):
        GameText.print(self.state_message, PLAYER_TURN_MESSAGE_X, PLAYER_TURN_MESSAGE_Y)

    def is_done(self):
        return self.state

    def verify_player_confirmation(self, events):
        pass

    def update_player_list(self):
        pass

    def show_confirm_button(self, screen, groups):
        pass
