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
                x = self.get_x()
                y = self.get_y()
                self.rect = self.image.get_rect()
                self.set_x(x)
                self.set_y(y)

        def get_x(self):
                return self.rect.x

        def get_y(self):
                return self.rect.y

        def set_x(self, x_position):
                self.rect.x = x_position

        def set_y(self, y_position):
                self.rect.y = y_position
