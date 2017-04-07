import pygame


# Create the game screen
class GameCanvas:
    __height = 0
    __width = 0

    def __init__(self, height, width):
        self.__height = height
        self.__width = width

    def start_screen(self, screen_name):
        screen = pygame.display.set_mode((self.__height, self.__width))
        pygame.display.set_caption(screen_name)
        return screen
