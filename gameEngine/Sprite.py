import pygame


# folder of sprite
image_resources = "../assets/"


# make a sprite game scene
class Sprite(pygame.sprite.Sprite):
        def __init__(self, filename):

                super(Sprite, self).__init__()
                self.image = pygame.image.load(image_resources +
                                               filename)
                self.rect = self.image.get_rect()

        def resize(self, width, height):

                self.image = pygame.transform.scale(self.image,
                                                    (width, height))

        def get_x(self):
                return self.rect.x

        def get_y(self):
                return self.rect.y

        def set_x(self, x_position):
                self.rect.x = x_position

        def set_y(self, y_position):
                self.rect.y = y_position
