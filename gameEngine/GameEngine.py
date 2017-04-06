import pygame
from gameEngine.GameCanvas import *
from sys import exit
from gameEngine.GameObject import *


SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600


class GameEngine:

    def run(self):

            pygame.init()

            all_sprites_list = pygame.sprite.Group()
            canvas = GameCanvas(SCREEN_WIDTH, SCREEN_HEIGHT)
            screen_name = "Start Game"
            canvas.start_screen(screen_name)

            gameObject = GameObject(60, 80, "sonic.png")

            canvas = GameCanvas(SCREEN_HEIGHT, SCREEN_HEIGHT)
            screen_name = "Start Game"
            screen = canvas.start_screen(screen_name)

            playerObject = GameObject(60, 80, "sonic.png")
            playerObject.rect.x = 160
            playerObject.rect.y = SCREEN_HEIGHT - 100

            # Add the gameObject to the list of objects
            all_sprites_list.add(playerObject)

            clock = pygame.time.Clock()

            while True:

                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            exit()
                        elif event.type == pygame.KEYDOWN:
                            if event.key == pygame.K_x:
                                playerObject.moveRight(10)

                    gameObject.drag_and_drop_mouse_movement(playerObject,
                                                            event)

                    all_sprites_list.draw(screen)
                    all_sprites_list.update()
                    pygame.display.flip()

                    clock.tick(60)

            pygame.quit()