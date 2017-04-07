import pygame


#make a sprite game scene
class Sprite(pygame.sprite.Sprite):
        def __init__(self, width, height, filename):

                super(Sprite, self).__init__()
                self.image = pygame.Surface([width, height])
                self.rect = self.image.get_rect()
                self.image = pygame.image.load(image_resources +
                                               filename)
                self.image = pygame.transform.scale(self.image, (width,
                                                                 height))
