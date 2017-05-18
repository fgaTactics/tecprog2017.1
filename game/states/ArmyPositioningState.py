import logging
from gameEngine.Mouse import *
from gameEngine.GameObject import *
from gameEngine.GameText import *
from game.pieces.DraggablePiece import *
from game.gameboard.PieceList import *

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

        logging.info("Creating state")
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
        logging.info("Creating State Complete")


    # Every state update is generalized as this two methods
    def update(self, events):
        logging.debug("Updating state")
        # Updates the list that belongs to the player who's turn it is.
        self.update_player_list(events)

        # Check if the player met the requirements to confirm the end of turn
        self.verify_player_confirmation(events)
        logging.debug("State's update Complete!")


    # Every state draw method is generalized as this two methods
    def draw(self, screen, groups):
        logging.debug("Drawing state")
        # Print the confirm button if the conditions of the turn are met
        self.show_confirm_button(screen, groups)

        # Print a message indicating which player turn it is
        self.show_player_turn_message()
        logging.debug("State's drawing complete")


    """ This method checks if the player clicked the confirm button that
is being shown if the conditions are met on show_confirm_button method.
this is called by this state children's verify_player_confirmation"""
    def verify_mouse_click_on_confirm(self, events):
        logging.debug("Verifying if the player clicked on confirm button")

        mouse = Mouse()

        # If the player confirms the end of turn, the state must end
        if(mouse.is_mouse_click(self.confirm_button, events)):
            logging.info("Player clicked confirm")
            self.state = COMPLETE
        else:
            logging.debug("Player didn't clicked confirm yet")
            # Do nothing
            pass

        logging.debug("Verifying complete")


    # Generic method to show the message overriden in each state
    def show_player_turn_message(self):
        logging.debug("Printing message informing player turn")

        # State message is defined in each state init
        GameText.print(self.state_message, PLAYER_TURN_MESSAGE_X, PLAYER_TURN_MESSAGE_Y)

        logging.debug("Message printed")


    # Using state requirements controls the drag of new pieces and turn end confirmation
    def verify_player_confirmation(self, events):

        # The player must meet the state requirements to confirm the piece choices
        if(self.check_player_turn_requirements()):

            # The player can't drag more pieces than the requirement defines
            DraggablePiece.set_drag_enable(False)
            logging.info("The Player can confirm the piece choices")

            # Even if the requirements are met, the player must click confirm
            self.verify_mouse_click_on_confirm(events)

        # Player can't click confirm, dragging new pieces is valid
        else:
            logging.debug("The Player can't confirm")
            DraggablePiece.set_drag_enable(True)


    # The confirm button is only exhibited if the player completes his piece choices
    def show_confirm_button(self, screen, groups):
        logging.debug("Verifying if the confirm button must be shown")

        # The player only see the button if he is done positioning X pieces
        if(self.check_player_turn_requirements()):
            logging.debug("The Player can see the confirm button")
            groups.add(self.confirm_button.sprite)

        # The player must position more pieces in board to see the button
        else:
            # Do nothing
            pass

    # ArmyPositionScene needs to know when to change states
    def is_done(self):
        logging.debug("State's state: " + str(self.state))
        return self.state

    # Abstract method to be implemented by each specific state
    def check_player_turn_requirements(self):
        pass

    # Abstract method to be implemented by each specific state
    def update_player_list(self):
        pass
