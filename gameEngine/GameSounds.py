import pygame
import logging

'''
* This class manage the sound of buttons and clicks in all the game
* Maked by students of software enginier on the dicipline Tecnicas de Programação
* Students of Universidade de Brasília
'''

# Adding constant to sounds path
SOUND_PATH = "../assets/sounds/"

# This class creates a controller sounds on game


class GameSounds:

    def __init__(self, sound_name):
        logging.info("Beggin of initialize method of game sound")
        self.sound_name = sound_name
        assert sound_name is not None, "Invalide sound name"
        logging.info("End of initialize method of game sound")

    def play_sound(self):
        try:
            logging.info("Playing sound button")
            # -- Play the sound --
            pygame.mixer.Sound(SOUND_PATH + self.sound_name).play()
            # -- End play the sound --
            logging.info("End of sound button")
        except:
            logging.info("Fail to open the sound")
