import pygame
import logging

# This class creates a controller to musics on game

# Adding constant to musics path
MUSIC_PATH = "../assets/music/"
PLAY_ONCE = 0
PLAY_LOOPING = -1


class GameMusic:


    def __init__(self, music_name):
        self.music_name = music_name
        pygame.mixer.init()

    def play_music(self):
        assert self.music_name != "", "INVALID NAME"

        try:
            logging.info("Load music" + self.music_name)
            pygame.mixer.music.load(MUSIC_PATH + self.music_name)

            logging.info("Play music" + self.music_name)
            pygame.mixer.music.play(PLAY_LOOPING)
        except:
            logging.info("Music file couldn't be found")

    def stop_music(self):
        pygame.mixer.music.stop()
