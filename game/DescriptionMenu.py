from gameEngine.GameObject import GameObject


FILENAME = "MYP.png"


class DescriptionMenu(GameObject):

    def __init__(self, x_position, y_position=14, width=210, height=170):
        super().__init__(x_position, y_position, width, height, FILENAME)
