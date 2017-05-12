import unittest
from gameEngine.GameCanvas import *

# All the following numeric constants are pixels units
CANVAS_WIDTH = 30
CANVAS_HEIGHT = 30
NEW_WIDTH = 30
NEW_HEIGHT = 30

# Tests for Game Canvas Class


class GameCanvasTests(unittest.TestCase):
    def setUp(self):
        self.canvas = GameCanvas(CANVAS_WIDTH, CANVAS_HEIGHT)

    def test_get_width(self):
        self.assertEqual(getattr(self.canvas, '_GameCanvas__width'), CANVAS_WIDTH)

    def test_get_height(self):
        self.assertEqual(getattr(self.canvas, '_GameCanvas__height'), CANVAS_HEIGHT)

    def test_set_width(self):
        setattr(self.canvas, '_GameCanvas__width', NEW_WIDTH)
        self.assertEqual(getattr(self.canvas, '_GameCanvas__width'), NEW_WIDTH)

    def test_set_height(self):
        setattr(self.canvas, '_GameCanvas__height', NEW_HEIGHT)
        self.assertEqual(getattr(self.canvas, '_GameCanvas__height'), NEW_HEIGHT)

if __name__ == '__main__':
        unittest.main()
