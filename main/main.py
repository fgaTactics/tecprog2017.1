
from gameEngine.GameEngine import *
from game.scenes.StartGameScene import *
from game.scenes.ClassSelectionScene import *

scene = StartGameScene("example", 1)
# scene = ClassSelectionScene("example", 1)
gameEngine = GameEngine()

gameEngine.add_scene(scene)

gameEngine.set_initial_scene("example")
gameEngine.run()
