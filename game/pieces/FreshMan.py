from game.pieces.BasicPiece import BasicPiece


class FreshMan(BasicPiece):

    def __init__(self, health=0, attack=0, rangeAttack=0, defense=0,
                 amount_of_moviment=0, penalty=0, hability="",
                 description="", x_position=0, y_position=0,
                 width=0, height=0, filename="", square=None, player=None):
                super().__init__(health, attack, rangeAttack, defense,
                                 amount_of_moviment, penalty,
                                 hability, description, x_position,
                                 y_position, width,
                                 height, filename, square, player)
                self.set_range(rangeAttack)
                self.set_x(x_position)
                self.set_y(x_position)

    def get_range(self):
        return self.rangeAttack

    def set_range(self, rangeAttack):
        self.rangeAttack = rangeAttack

    def set_x(self, x_position):
        self.x_position = x_position

    def get_x(self):
        return self.x_position

    def set_y(self, y_position):
        self.y_position = y_position

    def get_y(self):
        return self.y_position
