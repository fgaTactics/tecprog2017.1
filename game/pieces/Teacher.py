from game.pieces.BasicPiece import BasicPiece


class Teacher(BasicPiece):

    def __init__(self, x_position=0, y_position=0, health=0, attack=0, rangeAttack=0,
                 defense=0, amount_of_moviment=0, penalty=0, hability="", description="",
                 width=0, height=0, filename=""):
        super().__init__(x_position, y_position, health, attack, rangeAttack, defense,
                         amount_of_moviment, penalty,
                         hability, description, width,
                         height, filename)
