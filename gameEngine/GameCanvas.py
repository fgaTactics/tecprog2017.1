import pygame


class GameCanvas:
    __height = 0
    __width = 0

    def __init__(self, height, width):
        self.__height = height
        self.__width = width

    def startScreen(self):
        screen = pygame.display.set_mode((self.__height, self.__width))
        pygame.display.set_caption("Start Game")
