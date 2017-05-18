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

# Defining a state's state to control state change
RUNNING = False
COMPLETE = True

"""This class defines state's behaviour to be used in the ArmyPositioningScene.
They are used to control which player turn it is to select pieces, controlling then,
which pieces are updated and what are not, and which message is being shown."""


class ArmyPositioningState:

    # The states must receive the players list to control piece quantity
    def __init__(self, player1_piece_list, player2_piece_list):
        self.player1_piece_list = player1_piece_list
        self.player2_piece_list = player2_piece_list

        # States default state is running
        self.state = RUNNING

        # Variable to hold state's specific message to define player turn
        self.state_message = "Default message"

        # The button is the same for every state
        self.confirm_button = GameObject(CONFIRM_BUTTON_X, CONFIRM_BUTTON_Y,
                                         CONFIRM_BUTTON_WIDTH, CONFIRM_BUTTON_HEIGHT,
                                         CONFIRM_BUTTON_FILENAME)


    # Every state update is generalized as this two methods
    def update(self, events):
        # Updates the list that belongs to the player who's turn it is.
        self.update_player_list(events)

        # Check if the player met the requirements to confirm the end of turn
        self.verify_player_confirmation(events)


    # Every state draw method is generalized as this two methods
    def draw(self, screen, groups):
        # Print the confirm button if the conditions of the turn are met
        self.show_confirm_button(screen, groups)

        # Print a message indicating which player turn it is
        self.show_player_turn_message()


    """ This method checks if the player clicked the confirm button that
is being shown if the conditions are met on show_confirm_button method.
this is called by this state children's verify_player_confirmation"""
    def verify_mouse_click_on_confirm(self, events):
        mouse = Mouse()

        # If the player confirms the end of turn, the state must end
        if(mouse.is_mouse_click(self.confirm_button, events)):
            logging.info("Player clicked confirm")
            self.state = COMPLETE
        else:
            # Do nothing
            pass


    # Generic method to show the message overriden in each state
    def show_player_turn_message(self):
        # State message is defined in each state init
        GameText.print(self.state_message, PLAYER_TURN_MESSAGE_X, PLAYER_TURN_MESSAGE_Y)


    # ArmyPositionScene needs to know when to change states
    def is_done(self):
        return self.state


    # Abstract method to be implemented by each state
    def verify_player_confirmation(self, events):
        pass

    # Abstract method to be implemented by each state
    def update_player_list(self):
        pass

    # Abstract method to be implemented by each state
    def show_confirm_button(self, screen, groups):
        pass
