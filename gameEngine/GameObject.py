from gameEngine.Sprite import *

# This class creates a object that will be shown in the screen

FREQUENCY = 22050
SIZE = -16
CHANNELS = 1
BUFFER = 256


class GameObject:


    def __init__(self, x_position, y_position, width, height, filename):
        self.sprite = Sprite(filename)
        self.sprite.resize(width, height)
        self.set_width(width)
        self.set_height(height)
        self.set_x(x_position)
        self.set_y(y_position)
        pygame.mixer.pre_init(FREQUENCY, SIZE, CHANNELS, BUFFER)
        pygame.mixer.init()

    def draw(self, screen, groups):
        groups.add(self.sprite)

    def update(self, events):
        pass

    def get_width(self):
        return self.__width

    def set_width(self, width):
        assert(width > 0), "Can't have an invisible object"
        self.__width = width

    def get_height(self):
        return self.__height

    def set_height(self, height):
        assert(height > 0), "Can't have an invisible object"
        self.__height = height

    # Receive horizontal and vertical positioning of a game object
    def get_x(self):
        return self.sprite.get_x()

    def get_y(self):
        return self.sprite.get_y()


    # Set horizontal and vertical positioning of a game object
    def set_x(self, x_position):
        self.sprite.set_x(x_position)

    def set_y(self, y_position):
        self.sprite.set_y(y_position)
