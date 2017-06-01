import pygame
import logging

# This class creates a controller sounds on game

# Adding constant to sounds path
SOUND_PATH = "../assets/sounds/"


class GameSounds:

    def __init__(self, sound_name):
        self.sound_name = sound_name

    def play_sound(self):
        
