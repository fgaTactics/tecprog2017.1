from gameEngine.GameEngine import *
from game.scenes.StartGameScene import *
from game.scenes.ArmyPositioningScene import *
from game.scenes.ClassSelectionScene import *
from game.scenes.PieceInBoardScene import *
from game.pieces.Engineer import *
from game.pieces.FreshMan import *


engener = Engenner(health=0, attack=0, rangeAttack=0, defense=0,
                   amount_of_moviment=0, penalty=0,
                   hability="", description="",
                   x_position=0, y_position=0,
                   width=60, height=60, filename="MYP.png")

engenver = FreshMan(health=0, attack=0, rangeAttack=0, defense=0,
                    amount_of_moviment=0, penalty=0,
                    hability="", description="",
                    x_position=100, y_position=100,
                    width=60, height=60, filename="MYP.png")
pieces_list = []
pieces_list.append(engener)
pieces_list.append(engenver)
scene = PieceInBoardScene("Start Menu", 0, pieces_list)


gameEngine = GameEngine()

gameEngine.add_scene(scene)


gameEngine.set_initial_scene("Start Menu")
gameEngine.run()
