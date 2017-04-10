
from gameEngine.Scene import *
from gameEngine.GameObject import *


class StartGameScene(Scene):

    def __init__(self, name="DEFAULT", ID=666):
        super().__init__(name, ID)
        self.background = GameObject(200, 100, 400, 200, "logo.png")
        self.start_button = GameObject(300, 350, 200, 100,
                                       "start_button.png")

    def update(self):
        pass

    def draw(self, groups):
        groups.add(self.background.sprite)
        groups.add(self.start_button.sprite)
