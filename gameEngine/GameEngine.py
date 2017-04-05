import pygame
from gameEngine.GameCanvas import *
from sys import exit
from gameEngine.GameObject import *


class GameEngine:

    def run(self):
        pygame.init()

        # This colors just for see gameObject and spriteController
        WHITE = (255, 255, 255)
        GREEN = (20, 255, 140)
        GREY = (210, 210, 210)
        WHITE = (255, 255, 255)
        RED = (255, 0, 0)

        all_sprites_list = pygame.sprite.Group()

        gameObject = GameObject(WHITE, 60, 80)

        canvas = GameCanvas(800, 600)
        screen_name = "Start Game"
        screen = canvas.start_screen(screen_name)

        playerObject = GameObject(RED, 60, 80)
        playerObject.rect.x = 160
        playerObject.rect.y = 600 - 100

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

            gameObject.drag_and_drop_mouse_movement(playerObject, event)

            all_sprites_list.update()

            # Drawing on Screen
            screen.fill(GREEN)

            # Draw The Road
            pygame.draw.rect(screen, GREY, [40, 0, 400, 600])

            # Now let's draw all the sprites in one go.
            # (For now we only have 1 sprite!)
            all_sprites_list.draw(screen)

            # Refresh screen for
            pygame.display.flip()

            # Number of frames per secong e.g. 60
            clock.tick(60)

            pygame.quit()
