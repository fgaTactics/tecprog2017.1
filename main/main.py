from gameEngine.GameEngine import *
from game.scenes.StartGameScene import *
from game.scenes.ArmyPositioningScene import *
from game.scenes.ClassSelectionScene import *

scene = StartGameScene("Start Menu", 0)
scene2 = ClassSelectionScene("Class Selection", 1)
scene3 = ArmyPositioningScene("Army Positioning", 2)

gameEngine = GameEngine()

gameEngine.add_scene(scene)
gameEngine.add_scene(scene2)
gameEngine.add_scene(scene3)

gameEngine.set_initial_scene("Start Menu")
gameEngine.run()
