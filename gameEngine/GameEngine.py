import pygame
from gameEngine.GameCanvas import *
from sys import exit
from gameEngine.GameObject import *
from model.BasicPiece import *
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600


class GameEngine:
    def run(self):

            pygame.init()

            all_sprites_list = pygame.sprite.Group()
            canvas = GameCanvas(SCREEN_WIDTH, SCREEN_HEIGHT)
            screen_name = "Start Game"
            canvas.start_screen(screen_name)

            # Screen creation
            canvas = GameCanvas(SCREEN_HEIGHT, SCREEN_HEIGHT)
            screen_name = "Start Game"
            screen = canvas.start_screen(screen_name)

            # Game Object for screen
            playerObject = BasicPiece(10, 10, 10, 10, 10, 10, "Hability",
                                      "description", 60, 80, "sonic.png")
            playerObject.rect.x = 160
            playerObject.rect.y = SCREEN_HEIGHT - 100
        # Add the gameObject to the list of objects
        all_sprites_list.add(playerObject)

            # Add the gameObject to the list of objects
            all_sprites_list.add(playerObject)

        # Add the gameObject to the list of objects
        all_sprites_list.add(playerObject)
        playerObject.drag_and_drop_mouse_movement(playerObject, event)
            clock = pygame.time.Clock()

            while True:

                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            exit()
                        elif event.type == pygame.KEYDOWN:
                            if event.key == pygame.K_x:
                                playerObject.moveRight(10)

                    playerObject.drag_and_drop_mouse_movement(
                        playerObject, event)

                    all_sprites_list.draw(screen)
                    all_sprites_list.update()
                    pygame.display.flip()
                    clock.tick(60)

            # Drawing on Screen
            screen.fill(GREEN)

            # Draw The Road
            pygame.draw.rect(screen, GREY, [40, 0, 400, 600])

            # Now let's draw all the sprites in one go.
            # (For now we only have 1 sprite!)
            all_sprites_list.draw(screen)
            all_sprites_list.update()

            # Refresh screen
            pygame.display.flip()

            # Number of frames per secong e.g. 60
            clock.tick(60)

            pygame.quit()
