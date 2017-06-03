class SquareNotFoundError(Exception):
    def __init__(self):
        super.__init__(self, "There is no square available close to this" +
                       "drop to put the piece")
