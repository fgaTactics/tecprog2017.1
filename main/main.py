from gameEngine.GameEngine import *
from game.scenes.StartGameScene import *
from game.scenes.ArmyPositioningScene import *
from game.scenes.ClassSelectionScene import *
from game.scenes.PieceInBoardScene import *

scene = PieceInBoardScene("Start Menu", 0)


gameEngine = GameEngine()

gameEngine.add_scene(scene)


gameEngine.set_initial_scene("Start Menu")
gameEngine.run()
