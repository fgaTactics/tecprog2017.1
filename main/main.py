
from gameEngine.GameEngine import *
from game.scenes.StartGameScene import *
from game.scenes.ArmyPositioningScene import *

scene = StartGameScene("Start Menu", 0) 
scene2 = ArmyPositioningScene("Army Positioning", 1)

gameEngine = GameEngine()

gameEngine.add_scene(scene)
gameEngine.add_scene(scene2)

gameEngine.set_initial_scene("Start Menu")
gameEngine.run()
