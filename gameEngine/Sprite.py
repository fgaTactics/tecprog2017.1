import pygame

image_resources =  # Path of folder Assets on project

WHITE = (255, 255, 255)

class Sprite(pygame.sprite.Sprite):
        def __init__(self, width, height):

                super().__init__()
                self.image = pygame.Surface([width, height])
                #just use this color for test
                color = WHITE
                self.image.fill(color)
                self.image.set_colorkey(color)