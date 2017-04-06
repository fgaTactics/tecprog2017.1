

class BasicPiece:
    
    __health = 0
    __atack = 0
    __range = 0
    __defense = 0
    __amountOfMoviment=0
    __penality = None
    __hability = None
    __description = None
    
    def __init__(self,health, atack,range,defense,amountOfMoviment,penality,hability,description):
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
    
    # RAnge é palavra reservada , lascou
    def __setRange(self, range):
        self.__range = range
        
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
    
    def __setHability(self , hability):
        self.__hability = hability 
    
    def getDescription(self):
        return self.__description
    
    def __setDescription(self, description):
        self.__description = description
        
    