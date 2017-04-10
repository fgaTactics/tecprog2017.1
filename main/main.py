
from gameEngine.GameEngine import *
from game.scenes.StartGameScene import *

scene = StartGameScene("example", 1)

gameEngine = GameEngine()

gameEngine.add_scene(scene)

gameEngine.set_initial_scene("example")
gameEngine.run()
