import logging
import pygame
from time import sleep
from gameEngine.Scene import *
from gameEngine.GameObject import *
from gameEngine.Mouse import *
from gameEngine.GameEngine import *
from gameEngine.GameMusic import *
from gameEngine.GameSounds import *


# Sprite file names
BACKGROUND_IMAGE = "background.png"
LOGO_IMAGE = "logo.png"
START_BUTTON_IMAGE = "start_button.png"
OPTIONS_BUTTON_IMAGE = "start_button.png"
QUIT_BUTTON_IMAGE = "start_button.png"
ACTIVE_BUTTON_PREFIX = "active_"

# All the following constants are pixels units
# Background measurements
BACKGROUND_POS_X = 0
BACKGROUND_POS_Y = 0
BACKGROUND_WIDTH = 1199
BACKGROUND_HEIGHT = 600

# Logo measurements
LOGO_WIDTH = 600
LOGO_HEIGHT = 300
LOGO_POS_X = 300
LOGO_POS_Y = 80

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

# Music start scene
MUSIC_NAME = "menu_music.mp3"

""" This class draws the first screen of the game, containing buttons to start the game,to
the options menu and to quit the game"""


class StartGameScene(Scene):


    # Initialize logo and the interactive buttons
    def __init__(self, name="DEFAULT", ID=0):
        logging.info("Constructing Start Game Scene")

        super().__init__(name, ID)

        self.background = GameObject(BACKGROUND_POS_X,
                                     BACKGROUND_POS_Y,
                                     BACKGROUND_WIDTH,
                                     BACKGROUND_HEIGHT,
                                     BACKGROUND_IMAGE)

        self.logo = GameObject(LOGO_POS_X,
                               LOGO_POS_Y,
                               LOGO_WIDTH,
                               LOGO_HEIGHT,
                               LOGO_IMAGE)

        # Load and start music on scene
        self.start_game_scene_music = GameMusic(MUSIC_NAME)
        self.start_game_scene_music.play_music()

        # Create mouse interactive start game button
        self.inactive_start_button = GameObject(START_BUTTON_POS_X,
                                                START_BUTTON_POS_Y,
                                                START_BUTTON_WIDTH,
                                                START_BUTTON_HEIGHT,
                                                START_BUTTON_IMAGE)
        self.active_start_button = GameObject(START_BUTTON_POS_X,
                                              START_BUTTON_POS_Y,
                                              START_BUTTON_WIDTH,
                                              START_BUTTON_HEIGHT,
                                              ACTIVE_BUTTON_PREFIX +
                                              START_BUTTON_IMAGE)

        # Create mouse interactive options button
        self.inactive_options_button = GameObject(OPTIONS_BUTTON_POS_X,
                                                  REGULAR_BUTTON_POS_Y,
                                                  REGULAR_BUTTON_WIDTH,
                                                  REGULAR_BUTTON_HEIGHT,
                                                  OPTIONS_BUTTON_IMAGE)
        self.active_options_button = GameObject(OPTIONS_BUTTON_POS_X,
                                                REGULAR_BUTTON_POS_Y,
                                                REGULAR_BUTTON_WIDTH,
                                                REGULAR_BUTTON_HEIGHT,
                                                ACTIVE_BUTTON_PREFIX +
                                                OPTIONS_BUTTON_IMAGE)

        # Create mouse interactive quit game button
        self.inactive_quit_button = GameObject(QUIT_BUTTON_POS_X,
                                               REGULAR_BUTTON_POS_Y,
                                               REGULAR_BUTTON_WIDTH,
                                               REGULAR_BUTTON_HEIGHT,
                                               QUIT_BUTTON_IMAGE)
        self.active_quit_button = GameObject(QUIT_BUTTON_POS_X,
                                             REGULAR_BUTTON_POS_Y,
                                             REGULAR_BUTTON_WIDTH,
                                             REGULAR_BUTTON_HEIGHT,
                                             ACTIVE_BUTTON_PREFIX +
                                             QUIT_BUTTON_IMAGE)

        self.sound_button = GameSounds("")

        logging.info("Start Game Scene is ready")


    # Displays an animation when mouse cursor is over the object
    def mouse_animation(self, groups, inactive_element, active_element):
        logging.debug("Displaying animation when mouse is over the object")

        mouse = Mouse()
        if(mouse.is_mouse_over(inactive_element)):
            logging.debug("Exhibiting active button animation")

            groups.add(active_element.sprite)
        else:
            logging.debug("Exhibiting inactive button animation")

            groups.add(inactive_element.sprite)

        logging.debug("Animation displayed")

    # Define scene's buttons actions
    def update(self, events):

        logging.debug("Beginning Start Game scene's update method")
        mouse = Mouse()

        # Quit button action
        if(mouse.is_mouse_click(self.inactive_quit_button, events)):
            logging.debug("Quitting game")

            exit()
        # Start Game button action
        elif(mouse.is_mouse_click(self.inactive_start_button, events)):

            self.sound_button.play_sound()

            self.next_scene()
            logging.debug("Moving on to the next scene")
            gameEngine = GameEngine.get_instance()
            gameEngine.scene_manager.load_next_scene()
        else:
            # Nothing to Do
            pass

        logging.debug("Finishing Start Game scene's update method")

    # Show logo and buttons in the screen
    def draw(self, screen, groups):
        logging.debug("Beginning Start Game scene's draw method")
        groups.add(self.background.sprite)
        groups.add(self.logo.sprite)
        self.mouse_animation(groups, self.inactive_start_button,
                             self.active_start_button)
        self.mouse_animation(groups, self.inactive_options_button,
                             self.active_options_button)
        self.mouse_animation(groups, self.inactive_quit_button,
                             self.active_quit_button)

        logging.debug("Finishing Start Game scene's draw method")

    def next_scene(self):
        gameEngine = GameEngine.get_instance()
        gameEngine.scene_manager.load_next_scene()

