from model.BasicPiece import *
from gameEngine.GameEngine import *
from gameEngine.GameObject import *
from gameEngine.Sprite import *

basic = BasicPiece()
basic.setAtack(10)
print("atack",basic.getAtack())
gameEngine = GameEngine()
gameEngine.run()
