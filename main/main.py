
from gameEngine.GameEngine import *
from gameEngine.Scene import *

scene = Scene("example", 1)

gameEngine = GameEngine()

gameEngine.add_scene(scene)

gameEngine.set_initial_scene("example")
gameEngine.run()
