import pygame
from gameEngine.Scene import *
from gameEngine.GameObject import *
from gameEngine.Mouse import *
from gameEngine.GameEngine import *

# All the following constants are pixels units
# Logo measurements
LOGO_WIDTH = 500
LOGO_HEIGHT = 250
LOGO_POS_X = 350
LOGO_POS_Y = 150

# Regular buttons measurements
REGULAR_BUTTON_WIDTH = 200
REGULAR_BUTTON_HEIGHT = 100
REGULAR_BUTTON_POS_Y = 450
OPTIONS_BUTTON_POS_X = 250
QUIT_BUTTON_POS_X = 750

# Start button measurements
START_BUTTON_WIDTH = 300
START_BUTTON_HEIGHT = 150
START_BUTTON_POS_Y = 425
START_BUTTON_POS_X = 450

""" This class draws the first screen of the game, containing buttons to start the game,to
the options menu and to quit the game"""


class StartGameScene(Scene):

    # Initialize logo and the interactive buttons
    def __init__(self, name="DEFAULT", ID=0):
        super().__init__(name, ID)

        self.logo = GameObject(LOGO_POS_X,
                               LOGO_POS_Y,
                               LOGO_WIDTH,
                               LOGO_HEIGHT,
                               "logo.png")

        # Create mouse interactive start game button
        self.inactive_start_button = GameObject(START_BUTTON_POS_X,
                                                START_BUTTON_POS_Y,
                                                START_BUTTON_WIDTH,
                                                START_BUTTON_HEIGHT,
                                                "start_button.png")
        self.active_start_button = GameObject(START_BUTTON_POS_X,
                                              START_BUTTON_POS_Y,
                                              START_BUTTON_WIDTH,
                                              START_BUTTON_HEIGHT,
                                              "active_start_button.png")

        # Create mouse interactive options button
        self.inactive_options_button = GameObject(OPTIONS_BUTTON_POS_X,
                                                  REGULAR_BUTTON_POS_Y,
                                                  REGULAR_BUTTON_WIDTH,
                                                  REGULAR_BUTTON_HEIGHT,
                                                  "start_button.png")
        self.active_options_button = GameObject(OPTIONS_BUTTON_POS_X,
                                                REGULAR_BUTTON_POS_Y,
                                                REGULAR_BUTTON_WIDTH,
                                                REGULAR_BUTTON_HEIGHT,
                                                "active_start_button.png")

        # Create mouse interactive quit game button
        self.inactive_quit_button = GameObject(QUIT_BUTTON_POS_X,
                                               REGULAR_BUTTON_POS_Y,
                                               REGULAR_BUTTON_WIDTH,
                                               REGULAR_BUTTON_HEIGHT,
                                               "start_button.png")
        self.active_quit_button = GameObject(QUIT_BUTTON_POS_X,
                                             REGULAR_BUTTON_POS_Y,
                                             REGULAR_BUTTON_WIDTH,
                                             REGULAR_BUTTON_HEIGHT,
                                             "active_start_button.png")


    # Displays an animation when mouse cursor is over the object
    def mouse_animation(self, groups, inactive_element, active_element):
        mouse = Mouse()
        if(mouse.is_mouse_over(inactive_element)):
            groups.add(active_element.sprite)
        else:
            groups.add(inactive_element.sprite)


    # Define scene's buttons actions
    def update(self, events):
        mouse = Mouse()

        # Quit button action
        if(mouse.is_mouse_click(self.inactive_quit_button)):
            exit()
        # Start Game button action
        elif(mouse.is_mouse_click(self.inactive_start_button)):
            gameEngine = GameEngine.get_instance()
            gameEngine.scene_manager.load_next_scene()
        else:
            # Nothing to Do
            pass


    # Show logo and buttons in the screen
    def draw(self, screen, groups):
        groups.add(self.logo.sprite)
        self.mouse_animation(groups, self.inactive_start_button,
                             self.active_start_button)
        self.mouse_animation(groups, self.inactive_options_button,
                             self.active_options_button)
        self.mouse_animation(groups, self.inactive_quit_button,
                             self.active_quit_button)
