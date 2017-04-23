import pygame

# This class controls all game object sprites

# Sprites Folder
IMAGE_RESOURCES = "../assets/"


# make a sprite game scene
class Sprite(pygame.sprite.Sprite):

        def __init__(self, filename):
                super(Sprite, self).__init__()
                self.image = pygame.image.load(IMAGE_RESOURCES +
                                               filename)
                self.rect = self.image.get_rect()


        def resize(self, width, height):
                self.image = pygame.transform.scale(self.image,
                                                    (width, height))
