from gameEngine.GameEngine import *
from game.scenes.StartGameScene import *
from game.scenes.ArmyPositioningScene import *
from game.scenes.ClassSelectionScene import *
from game.scenes.PieceInBoardScene import *
from game.pieces.Engineer import *
from game.pieces.FreshMan import *
from game.scenes.MovePieceScene import *



scene = StartGameScene("Start Menu", 0)
scene2 = ClassSelectionScene("Class Selection", 1)
scene3 = ArmyPositioningScene("Army Positioning", 2)
# scene4 = PieceInBoardScene("Start Menu", 0)
scene5 = MovePieceScene("Moving", 4)

gameEngine = GameEngine()
gameEngine.add_scene(scene)
gameEngine.add_scene(scene2)
gameEngine.add_scene(scene3)
gameEngine.add_scene(scene5)



gameEngine.set_initial_scene("Moving")
gameEngine.run()
