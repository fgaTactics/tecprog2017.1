import unittest
from gameEngine.GameObject import *


class GameObjectTests(unittest.TestCase):
    def setUp(self):
        self.game_object = GameObject(30, 40, 50, 50, "start_button.png")

    def test_get_x(self):
        self.assertEqual(self.game_object.get_x(), 30)

    def test_get_y(self):
        self.assertEqual(self.game_object.get_y(), 40)

    def test_set_x(self):
        self.game_object.set_x(10)
        self.assertEqual(self.game_object.get_x(), 10)

    def test_set_y(self):
        self.game_object.set_y(5)
        self.assertEqual(self.game_object.get_y(), 5)

if __name__ == '__main__':
        unittest.main()
