from game.pieces.BasicPiece import BasicPiece


class Engenner(BasicPiece):

    def __init__(self, health=0, attack=0, rangeAttack=0, defense=0,
                 amount_of_moviment=0, penalty=0,
                 hability="", description="", width=0,
                 height=0, filename=""):
        super().__init__(health, attack, rangeAttack, defense,
                         amount_of_moviment, penalty,
                         hability, description, width,
                         height, filename)
