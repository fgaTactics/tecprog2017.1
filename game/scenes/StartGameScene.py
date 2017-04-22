import pygame
from gameEngine.Scene import *
from gameEngine.GameObject import *
from gameEngine.Mouse import *

# All the following constants are pixels units
# Logo measurements
LOGO_WIDTH = 500
LOGO_HEIGHT = 250
LOGO_POS_X = 150
LOGO_POS_Y = 150

# Regular buttons measurements
REGULAR_BUTTON_WIDTH = 200
REGULAR_BUTTON_HEIGHT = 100
REGULAR_BUTTON_POS_Y = 450
OPTIONS_BUTTON_POS_X = 50
QUIT_BUTTON_POS_X = 550

# Start button measurements
START_BUTTON_WIDTH = 300
START_BUTTON_HEIGHT = 150
START_BUTTON_POS_Y = 425
START_BUTTON_POS_X = 250

"""This class show the first screen of the game
"""


class StartGameScene(Scene):

    def __init__(self, name="DEFAULT", ID=0):
        super().__init__(name, ID)


        self.logo = GameObject(LOGO_POS_X,
                               LOGO_POS_Y,
                               LOGO_WIDTH,
                               LOGO_HEIGHT,
                               "logo.png")

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


    def update(self, events):
        mouse = Mouse()

        # Quit button action
        if(mouse.is_mouse_click(self.inactive_quit_button)):
            exit()
        else:
            # Nothing to Do
            pass

    def draw(self, screen, groups):
        groups.add(self.logo.sprite)
        self.mouse_animation(groups, self.inactive_start_button,
                             self.active_start_button)
        self.mouse_animation(groups, self.inactive_options_button,
                             self.active_options_button)
        self.mouse_animation(groups, self.inactive_quit_button,
                             self.active_quit_button)
