
from gameEngine.Scene import *
from gameEngine.GameObject import *
IMAGE_WIDTH = 100
IMAGE_HEIGHT = 100


# Select the class which the player wants to fight for
class ClassSelectionScene(Scene):

    def __init__(self, name="DEFAULT", ID=666):
        super().__init__(name, ID)

        self.class_aerospace = GameObject(50, 100, IMAGE_WIDTH, IMAGE_HEIGHT,
                                          "aerospace_class.png")
        self.class_automotive = GameObject(350, 100, IMAGE_WIDTH, IMAGE_HEIGHT,
                                           "automotive_class.png")
        self.class_eletronic = GameObject(650, 100, IMAGE_WIDTH, IMAGE_HEIGHT,
                                          "eletronic_class.png")
        self.class_energy = GameObject(200, 400, IMAGE_WIDTH, IMAGE_HEIGHT,
                                       "energy_class.png")
        self.class_software = GameObject(500, 400, IMAGE_WIDTH, IMAGE_HEIGHT,
                                         "software_class.png")

    def update(self):
        pass

    def draw(self, groups):
        groups.add(self.class_aerospace.sprite)
        groups.add(self.class_automotive.sprite)
        groups.add(self.class_eletronic.sprite)
        groups.add(self.class_energy.sprite)
        groups.add(self.class_software.sprite)
