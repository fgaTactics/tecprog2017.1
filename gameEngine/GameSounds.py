import pygame
import logging

# This class creates a controller sounds on game

# Adding constant to sounds path
SOUND_PATH = "../assets/sounds/"


class GameSounds:

    def __init__(self, sound_name):
        logging.info("Beggin of initialize method of game sound")
        self.sound_name = sound_name
        logging.info("End of initialize method of game sound")

    def play_sound(self):
        logging.info("Playing sound button")
        pygame.mixer.Sound(SOUND_PATH + self.sound_name).play()
        logging.info("End of sound button")
