
from gameEngine.GameEngine import *
from game.scenes.StartGameScene import *
from game.scenes.GameBoardScene import *
from game.scenes.ArmyPositioningScene import *
scene = ArmyPositioningScene("example", 1)

gameEngine = GameEngine()

gameEngine.add_scene(scene)

gameEngine.set_initial_scene("example")
gameEngine.run()
