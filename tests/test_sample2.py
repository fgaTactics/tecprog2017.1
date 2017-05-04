import unittest
from gameEngine.GameCanvas import *

class GameCanvasTests(unittest.TestCase):
    canvas = GameCanvas(30, 30)

    def get_width_test(self):
        self.assertEqual(canvas._GameCanvas__width, 30)
        
    def get_height_test(self):
        self.assertEqual(canvas._GameCanvas__height, 30)

if __name__ == '__main__':
        unittest.main()
