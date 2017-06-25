from game.pieces.BasicPiece import BasicPiece

FILENAME = "pieces/engineer.jpg"

HEALTH = 10
ATTACK = 2
DEFENSE = 2
AMOUNT_OF_MOVIMENT = 2
DESCRIPTION = "Engineer"


class Engineer(BasicPiece):


    def __init__(self, x_position, y_position, width, height, player=None, square=None):
        assert (x_position > 0 and x_position < 1200), \
            "Can't create a piece outside the game screen"
        assert (y_position > 0 and y_position < 600), \
            "Can't create a piece outside the game screen"
        assert (width > 0 and height > 0), "Can't create an invisible piece"
        assert square != None, "Can't have a piece without a square"
        assert player != None, "A piece must belong to a player"

        super().__init__(x_position, y_position, width, height, FILENAME, player, square)


    def initialize_status(self):
        self.set_health(HEALTH)
        self.set_attack(ATTACK)
        self.set_defense(DEFENSE)
        self.set_amount_of_moviment(AMOUNT_OF_MOVIMENT)
        self.set_description(DESCRIPTION)
