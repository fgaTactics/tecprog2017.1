import unittest
from gameEngine.GameObject import *

# All the following numeric constants are pixels units
X_POSITION = 30
Y_POSITION = 40
NEW_X = 10
NEW_Y = 5
WIDTH = 50
HEIGHT = 50
FILENAME = "start_button.png"

# Tests for Game Object Class


class GameObjectTests(unittest.TestCase):
    def setUp(self):
        self.game_object = GameObject(X_POSITION, Y_POSITION, WIDTH, HEIGHT, FILENAME)

    def test_get_x(self):
        self.assertEqual(self.game_object.get_x(), X_POSITION)

    def test_get_y(self):
        self.assertEqual(self.game_object.get_y(), Y_POSITION)

    def test_set_x(self):
        self.game_object.set_x(NEW_X)
        self.assertEqual(self.game_object.get_x(), NEW_X)

    def test_set_y(self):
        self.game_object.set_y(NEW_Y)
        self.assertEqual(self.game_object.get_y(), NEW_Y)

if __name__ == '__main__':
        unittest.main()
