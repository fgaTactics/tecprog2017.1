from gameEngine.GameObject import GameObject


class BasicPiece(GameObject):

    def __init__(self, health=0, atack=0, rangeAtack=0, defense=0,
                 amountOfMoviment=0, penality=0,
                 hability=None, description=None, wight=0,
                 height=0, filename=None):
        super().__init__(wight, height, filename)
        self.__setHealth(health)
        self.__setAtack(atack)
        self.__setDefense(defense)
        self.__setAmountOfMoviment(amountOfMoviment)
        self.__setPenatily(penality)
        self.__setHability(hability)
        self.__setDescription(description)

    def getHealth(self):
        return self.__health

    def __setHealth(self, health):
        self.__health = health

    def getAtack(self):
        return self.__atack

    def __setAtack(self, atack):
        self.__atack = atack

    def getRange(self):
        return self.__range

    def __setRange(self, rangeAtack):
        self.__range = rangeAtack

    def getDefense(self):
        return self.__defense

    def __setDefense(self, defense):
        self.__defense = defense

    def getAmountOfMoviment(self):
        return self.__amountOfMoviment

    def __setAmountOfMoviment(self, amountOfMoviment):
        self.__amountOfMoviment = amountOfMoviment

    def getPenality(self):
        return self.__penality

    def __setPenatily(self, penality):
        self.__penality = penality

    def getHability(self):
        return self.__hability

    def __setHability(self, hability):
        self.__hability = hability

    def getDescription(self):
        return self.__description

    def __setDescription(self, description):
        self.__description = description
