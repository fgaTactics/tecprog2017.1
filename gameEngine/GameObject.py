
from gameEngine.Sprite import *

class GameObject(SpriteController):
    
    def __init__(self, color, width, height):
        super().__init__(width,height)
        self.width = width
        self.height = height
        self.color = color
        #just use for test
        pygame.draw.rect(self.image, self.color, [0, 0, self.width, self.height])
        self.rect = self.image.get_rect()


    #movement sprit with mouse
    def drag_and_drop_mouse_movement(self, playerGameObject, event):
        if pygame.mouse.get_pressed()[0]:
            mousePosicionX, mousePosicionY = event.pos
            if playerGameObject.rect.collidepoint(mousePosicionX, mousePosicionY):
                playerGameObject.rect.x = mousePosicionX - playerGameObject.rect.width / 2
                playerGameObject.rect.y = mousePosicionY - playerGameObject.rect.height / 2
                
    def moveRight(self, pixels):
        self.rect.x += pixels

    def moveLeft(self, pixels):
        self.rect.x -= pixels    