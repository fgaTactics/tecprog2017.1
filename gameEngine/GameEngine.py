import pygame
from gameEngine.GameCanvas import *
from sys import exit
from gameEngine.GameObject import *
from sceneManager.SceneManager import *
from model.BasicPiece import *
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
NUMBER_OF_FRAMES = 60


class GameEngine:

    def __init__(self):
        # Initialize Scene Manager
        self.scene_manager = SceneManager()

    def add_scene(self, scene):
        self.scene_manager.add_scene(scene)

    def set_initial_scene(self, scene_name):
        self.scene_manager.load_scene(scene_name)

    def run(self):

            pygame.init()

            # Screen creation
            canvas = GameCanvas(SCREEN_HEIGHT, SCREEN_HEIGHT)
            screen_name = "Start Game"
            screen = canvas.start_screen(screen_name)

            clock = pygame.time.Clock()

            while True:

                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            exit()
                        else:
                            # Do Nothing
                            pass

                    # Move the objects in the scene
                    self.scene_manager.current_scene.update()

                    # Draw all the objects in the scene
                    self.scene_manager.current_scene.draw(screen)

                    # Refresh screen
                    pygame.display.flip()

                    # Number of frames per secong e.g. 60
                    clock.tick(NUMBER_OF_FRAMES)
