
from gameEngine.Scene import *
from gameEngine.GameObject import *
from gameEngine.Mouse import *

IMAGE_WIDTH = 100
IMAGE_HEIGHT = 100

# Constants to define class' image position on screen
POSITION_X_AEROSPACE = 50
POSITION_X_AUTOMOTIVE = 350
POSITION_X_ELETRONIC = 650
POSITION_X_ENERGY = 200
POSITION_X_SOFTWARE = 500

POSITION_Y_AEROSPACE = 100
POSITION_Y_AUTOMOTIVE = 100
POSITION_Y_ELETRONIC = 100
POSITION_Y_ENERGY = 400
POSITION_Y_SOFTWARE = 400


# Select the class wich the player wants to fight for
class ClassSelectionScene(Scene):

    def __init__(self, name="DEFAULT", ID=666):
        super().__init__(name, ID)

        self.class_aerospace = GameObject(POSITION_X_AEROSPACE,
                                          POSITION_Y_AEROSPACE,
                                          IMAGE_WIDTH,
                                          IMAGE_HEIGHT,
                                          "aerospace_class.png")

        self.class_automotive = GameObject(POSITION_X_AUTOMOTIVE,
                                           POSITION_Y_AUTOMOTIVE,
                                           IMAGE_WIDTH,
                                           IMAGE_HEIGHT,
                                           "automotive_class.png")

        self.class_eletronic = GameObject(POSITION_X_ELETRONIC,
                                          POSITION_Y_ELETRONIC,
                                          IMAGE_WIDTH,
                                          IMAGE_HEIGHT,
                                          "eletronic_class.png")

        self.class_energy = GameObject(POSITION_X_ENERGY,
                                       POSITION_Y_ENERGY,
                                       IMAGE_WIDTH,
                                       IMAGE_HEIGHT,
                                       "energy_class.png")

        self.class_software = GameObject(POSITION_X_SOFTWARE,
                                         POSITION_Y_SOFTWARE,
                                         IMAGE_WIDTH,
                                         IMAGE_HEIGHT,
                                         "software_class.png")

    def update(self, event):
        mouse = Mouse()

        # Check where player click to select class
        if (mouse.is_mouse_over(self.class_aerospace) and
            mouse.is_mouse_click(self.class_aerospace)):
            print("Você escolheu Aerospacial")
        elif (mouse.is_mouse_over(self.class_automotive) and
              mouse.is_mouse_click(self.class_automotive)):
            print("Você escolheu Automotiva")
        elif (mouse.is_mouse_over(self.class_eletronic) and
              mouse.is_mouse_click(self.class_eletronic)):
            print("Você escolheu Eletrônica")
        elif (mouse.is_mouse_over(self.class_energy) and
              mouse.is_mouse_click(self.class_energy)):
            print("Você escolheu Energia")
        elif (mouse.is_mouse_over(self.class_software) and
              mouse.is_mouse_click(self.class_software)):
            print("Você escolheu Software")
        else:
            # Nothing to do
            pass

    def draw(self, screen, groups):
        groups.add(self.class_aerospace.sprite)
        groups.add(self.class_automotive.sprite)
        groups.add(self.class_eletronic.sprite)
        groups.add(self.class_energy.sprite)
        groups.add(self.class_software.sprite)