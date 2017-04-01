import pygame



WHITE = (255, 255, 255)

class SpriteController(pygame.sprite.Sprite):
        
        def __init__(self, width, height):
                super().__init__()
                self.image = pygame.Surface([width, height])
                #just use this color for test
                color = WHITE
                self.image.fill(color)
                self.image.set_colorkey(color)