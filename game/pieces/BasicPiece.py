import logging
from pygame import *
from gameEngine.GameObject import GameObject
from gameEngine.Mouse import *
from game.gameboard.PieceMenu import *

GREY = (150, 150, 150)
WHITE = (255, 255, 255)

"""This class is a model for the game pieces"""


class BasicPiece(GameObject):


    def __init__(self, health=1, attack=1, rangeAttack=1, defense=1,
                 amount_of_moviment=1, penalty=1,
                 hability="hability", description="description",
                 x_position=1, y_position=1, width=1,
                 height=1, filename="filename", square=None, player=None):
        super().__init__(x_position, y_position, width, height, filename)
        self.set_health(health)
        self.set_attack(attack)
        self.set_defense(defense)
        self.set_amount_of_moviment(amount_of_moviment)
        self.set_penalty(penalty)
        self.set_hability(hability)
        self.set_description(description)
        self.set_square(square)
        self.set_player(player)
        # All pieces on game have a option's menu
        self.menu = PieceMenu.get_piece_menu()

    def draw(self, screen, groups):
        groups.add(self.sprite)

    def update(self, event):
        mouse = Mouse()
        # Verify if player is press space to close options' menu
        if(mouse.is_mouse_click(self.get_square(), event)):
            self.menu.open()
        else:
            # Nothing to do
            pass

    def get_health(self):
        return self.__health

    def set_health(self, health):
        assert health != 0, "Invalide amount of health"
        self.__health = health
        assert self.__health == health, "Error on the health parametrer passage"

    def get_attack(self):
        return self.__attack

    def set_attack(self, attack):
        assert attack != 0, "Invalide amount of attack"
        self.__attack = attack
        assert self.__attack == attack, "Error on the attack parametrer passage"

    def get_range(self):
        return self.__range

    def set_range(self, rangeAttack):
        assert rangeAttack != 0, "Invalide quantitie of range attack"
        self.__rangeAttack = rangeAttack
        assert self.__rangeAttack == rangeAttack, "Error on the range attack parameter"

    def get_defense(self):
        return self.__defense

    def set_defense(self, defense):
        assert defense != 0, "Invalide amount of defense"
        self.__defense = defense
        assert self.__defense == defense, "Error on the defense parametrer passage"

    def get_amount_of_moviment(self):
        return self.__amount_of_moviment

    def set_amount_of_moviment(self, amount_of_moviment):
        assert amount_of_moviment != 0, "Invalide amount of moviment"
        self.__amount_of_moviment = amount_of_moviment
        assert self.__amount_of_moviment == amount_of_moviment, "amount of moviment error"

    def get_penality(self):
        return self.__penalty

    def set_penalty(self, penalty):
        assert penalty != 0, "Invalide quantitie of penalty"
        self.__penalty = penalty
        assert self.__penalty == penalty, "Error on the penalty parametrer passage"

    def get_hability(self):
        return self.__hability

    def set_hability(self, hability):
        assert hability != 0, "Invalide quantitie of hability"
        self.__hability = hability
        assert self.__hability == hability, "Error on the hability parametrer passage"

    def get_description(self):
        return self.__description

    def set_description(self, description):
        assert description is not None, "Invalide description"
        self.__description = description
        assert self.__description == description, "description parametrer error"

    def get_square(self):
        return self.__square

    def set_square(self, square):
        self.__square = square
        assert self.__square == square, "Error on the square parametrer passage"

    def get_player(self):
        return self.__player

    def set_player(self, player):
        self.__player = player
        assert self.__player == player, "Error on the player parametrer passage"
