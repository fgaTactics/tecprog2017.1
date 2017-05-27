import pygame


class GameSounds:

    def __init__(self, music_name):
        self.music_name = music_name

    def play_music(self):
        pygame.init()
        pygame.mixer.init()
        pygame.mixer.music.load(self.music_name)
        pygame.mixer.music.play()

    def stop_music(self):
        pygame.mixer.music.stop()
