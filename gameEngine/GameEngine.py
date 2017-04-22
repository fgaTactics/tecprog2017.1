import pygame
from gameEngine.GameCanvas import *
from sys import exit
from gameEngine.GameObject import *
from gameEngine.SceneManager import *
from game.pieces.BasicPiece import *

SCREEN_WIDTH = 1199
SCREEN_HEIGHT = 600
NUMBER_OF_FRAMES = 60


class GameEngine:
    instance = None

    def __init__(self):
        GameEngine.instance = self;
        self.scene_manager = SceneManager()
    
    @classmethod
    def get_instance(cls):
        return cls.instance

    def add_scene(self, scene):
        self.scene_manager.add_scene(scene)

    def set_initial_scene(self, scene_name):
        self.scene_manager.load_scene(scene_name)

    def run(self):

            pygame.init()

            # Screen creation
            canvas = GameCanvas(SCREEN_WIDTH, SCREEN_HEIGHT)
            screen_name = "Start Game"
            screen = canvas.start_screen(screen_name)

            clock = pygame.time.Clock()

            while True:

                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            exit()
                        else:
                            self.scene_manager.current_scene.update(event)

                    # Draw all the objects in the scene
                    groups = pygame.sprite.Group()
                    self.scene_manager.current_scene.draw(screen, groups)

                    groups.draw(screen)
                    groups.update()

                    # Refresh screen
                    pygame.display.flip()

                    # Number of frames per secong e.g. 60
                    clock.tick(NUMBER_OF_FRAMES)
