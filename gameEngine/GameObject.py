
from gameEngine.Sprite import *


class GameObject(Sprite):

    def __init__(self, width, height, filename):
        super().__init__(width, height, filename)
        self.width = width
        self.height = height

    # Movement sprite with mouse
    def drag_and_drop_mouse_movement(self, playerGameObject, event):

        player_width = playerGameObject.rect.width / 2
        player_height = playerGameObject.rect.height / 2

        if pygame.mouse.get_pressed()[0]:
            mousePosicionX, mousePosicionY = event.pos
            if playerGameObject.rect.collidepoint(mousePosicionX,
                                                  mousePosicionY):
                playerGameObject.rect.x = mousePosicionX - player_width
                playerGameObject.rect.y = mousePosicionY - player_height

    def move_right(self, pixels):
        self.rect.x += pixels

    def move_left(self, pixels):
        self.rect.x -= pixels

    def draw(self, tela):
        groups = pygame.sprite.Group()
        groups.add(self)
        groups.draw(tela)
        groups.update()
