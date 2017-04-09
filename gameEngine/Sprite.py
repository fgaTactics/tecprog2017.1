import pygame
import pygame


# folder of sprite
image_resources = "../assets/"


class Sprite(pygame.sprite.Sprite):
        def __init__(self, filename):

                super(Sprite, self).__init__()
                self.image = pygame.image.load(image_resources +
                                               filename)
                self.rect = self.image.get_rect()

        def resize(self, width, height):

                self.image = pygame.transform.scale(self.image, (width, height))
