import pygame
from gameEngine.GameCanvas import *
from sys import exit
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600


class GameEngine:

    def run(self):
        pygame.init()

        canvas = GameCanvas(SCREEN_WIDTH, SCREEN_HEIGHT)
        screen_name = "Start Game"
        canvas.start_screen(screen_name)

        while True:

            for event in pygame.event.get():

                if(event.type != pygame.QUIT):
                    # do nothing

                    pygame.display.update()

                else:
                    exit()
