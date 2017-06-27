from game.pieces.BasicPiece import BasicPiece


class Engineer(BasicPiece):

    def __init__(self, health=1, attack=1, rangeAttack=1, defense=1,
                 amount_of_moviment=1, penalty=1, hability="hability",
                 description="description", x_position=1, y_position=1,
                 width=1, height=1, filename="filename", square=None, player=None):
                super().__init__(health, attack, rangeAttack, defense,
                                 amount_of_moviment, penalty,
                                 hability, description, x_position,
                                 y_position, width,
                                 height, filename, square, player)
