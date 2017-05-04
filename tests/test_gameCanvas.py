import unittest
from gameEngine.GameCanvas import *


class GameCanvasTests(unittest.TestCase):
    def setUp(self):
        self.canvas = GameCanvas(30, 30)

    def test_get_width(self):
        self.assertEqual(getattr(self.canvas, '_GameCanvas__width'), 30)

    def test_get_height(self):
        self.assertEqual(getattr(self.canvas, '_GameCanvas__height'), 30)

    def test_set_width(self):
        setattr(self.canvas, '_GameCanvas__width', 8)
        self.assertEqual(getattr(self.canvas, '_GameCanvas__width'), 8)

    def test_set_height(self):
        setattr(self.canvas, '_GameCanvas__height', 10)
        self.assertEqual(getattr(self.canvas, '_GameCanvas__height'), 10)

if __name__ == '__main__':
        unittest.main()
