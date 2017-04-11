import pygame
from gameEngine.Scene import *
from gameEngine.GameObject import *
from gameEngine.Mouse import *


class StartGameScene(Scene):

    def __init__(self, name="DEFAULT", ID=666):
        super().__init__(name, ID)
        self.background = GameObject(150, 150, 500, 250, "logo.png")

        self.inactive_start_button = GameObject(250, 425, 300, 150,
                                                "start_button.png")
        self.active_start_button = GameObject(250, 425, 300, 150,
                                              "active_start_button.png")

        self.inactive_options_button = GameObject(50, 450, 200, 100,
                                                  "start_button.png")
        self.active_options_button = GameObject(50, 450, 200, 100,
                                                "active_start_button.png")

        self.inactive_quit_button = GameObject(550, 450, 200, 100,
                                               "start_button.png")
        self.active_quit_button = GameObject(550, 450, 200, 100,
                                             "active_start_button.png")

    def mouse_animation(self, groups, inactive_element, active_element):
        mouse = Mouse()
        if(mouse.is_mouse_over(inactive_element)):
            groups.add(active_element.sprite)
        else:
            groups.add(inactive_element.sprite)

    def update(self):
        mouse = Mouse()
        if(mouse.is_mouse_over(self.inactive_quit_button) and
           mouse.is_mouse_click(self.inactive_quit_button)):
            exit()
        else:
            # Nothing to Do
            pass

    def draw(self, groups):
        groups.add(self.background.sprite)
        self.mouse_animation(groups, self.inactive_start_button,
                             self.active_start_button)
        self.mouse_animation(groups, self.inactive_options_button,
                             self.active_options_button)
        self.mouse_animation(groups, self.inactive_quit_button,
                             self.active_quit_button)
