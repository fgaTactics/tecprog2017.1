
from gameEngine.GameEngine import *
from game.scenes.StartGameScene import *
from game.scenes.GameBoardScene import *

scene = GameBoardScene("example", 1)

gameEngine = GameEngine()

gameEngine.add_scene(scene)

gameEngine.set_initial_scene("example")
gameEngine.run()
