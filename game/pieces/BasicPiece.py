import logging
from pygame import *
from gameEngine.GameObject import GameObject
from gameEngine.Mouse import *
from game.gameboard.PieceMenu import *
from game.pieces.LifeBar import *

GREY = (150, 150, 150)
WHITE = (255, 255, 255)

"""This class is a model for the game pieces"""


class BasicPiece(GameObject):


    def __init__(self, health=0, attack=0, rangeAttack=0, defense=0,
                 amount_of_moviment=0, penalty=0,
                 hability="", description="", x_position=0, y_position=0, width=0,
                 height=0, filename="", square=None, player=None):
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
        self.life_bar = LifeBar(self.get_x(), self.get_y(), health)


    def draw(self, screen, groups):
        groups.add(self.sprite)
        self.life_bar.draw(screen, groups)


    def update(self, event):
        mouse = Mouse()
        # Verify if player is press space to close options' menu
        if(mouse.is_mouse_click(self.get_square(), event)):
            self.menu.open()
        else:
            # Do nothing
            pass


    def verify_menu_opening(self, event):
        mouse = Mouse()
        if(mouse.is_mouse_click(self, event)):
            self.menu.open(self)
        else:
            # Do nothing
            pass


    def take_damage(self, life_lost):
        new_health = self.get_health() - life_lost

        if(new_health > 0):
            self.set_health(new_health)
        else:
            self.set_health(0)

        self.life_bar.update_life(self.get_health())
    
    def get_health(self):
        return self.__health

    def set_health(self, health):
        self.__health = health

    def get_attack(self):
        return self.__attack

    def set_x(self, x_position):
        super().set_x(x_position)
        


    def set_y(self, y_position):
        super().set_y(y_position)

    def set_attack(self, attack):
        self.__attack = attack

    def get_range(self):
        return self.__range

    def set_range(self, rangeAttack):
        self.__rangeAttack = rangeAttack

    def get_defense(self):
        return self.__defense

    def set_defense(self, defense):
        self.__defense = defense

    def get_amount_of_moviment(self):
        return self.__amount_of_moviment

    def set_amount_of_moviment(self, amount_of_moviment):
        self.__amount_of_moviment = amount_of_moviment

    def get_penality(self):
        return self.__penalty

    def set_penalty(self, penalty):
        self.__penalty = penalty

    def get_hability(self):
        return self.__hability

    def set_hability(self, hability):
        self.__hability = hability

    def get_description(self):
        return self.__description

    def set_description(self, description):
        self.__description = description

    def get_square(self):
        return self.__square

    def set_square(self, square):
        self.__square = square

    def get_player(self):
        return self.__player

    def set_player(self, player):
        self.__player = player
