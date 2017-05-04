import unittest
from gameEngine.GameCanvas import *


class GameCanvasTests(unittest.TestCase):
    def setUp(self):
        self.canvas = GameCanvas(30, 30)

    def test_get_width(self):
        self.assertEqual(self.canvas._GameCanvas__width, 30)

    def test_get_height(self):
        self.assertEqual(self.canvas._GameCanvas__height, 30)

if __name__ == '__main__':
        unittest.main()
