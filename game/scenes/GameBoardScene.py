from gameEngine.Scene import *
from gameEngine.GameObject import *

class GameBoardScene(Scene):
    
    def __init__(self,name="DEFAULT",ID=0):
        super().__init__(name,ID)
        self.board_game = GameObject(0, 0, 800, 480, 
                                    "board_game.png")
        
    def draw(self, groups,screen):
        groups.add(self.board_game.sprite)
        