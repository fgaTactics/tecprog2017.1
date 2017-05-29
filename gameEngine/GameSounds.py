import pygame
import logging

# This class creates a controller to musics and sounds on game

# Adding constant to musics path
MUSIC_PATH = "../assets/sounds/"


class GameSounds:

    def __init__(self, music_name):
        self.music_name = music_name

    def play_music(self):
        assert self.music_name != "", "INVALID NAME"

        logging.info("Load music" + self.music_name)
        pygame.mixer.init()
        pygame.mixer.music.load(MUSIC_PATH + self.music_name)

        logging.info("Play music" + self.music_name)
        pygame.mixer.music.play()

    def stop_music(self):
        pygame.mixer.music.stop()
