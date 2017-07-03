import logging
from abc import ABC, abstractmethod
from pygame import *
from gameEngine.GameObject import GameObject
from gameEngine.Mouse import *
from game.gameboard.PieceMenu import *
from game.pieces.LifeBar import *
from gameEngine.GameSounds import *

GREY = (150, 150, 150)
WHITE = (255, 255, 255)

"""This class is an abstract model for the game pieces"""


class BasicPiece(GameObject, ABC):

    def __init__(self, x_position=0, y_position=0, width=0, height=0,
                 filename="default", player=None, square=None):
        assert (filename != "default"), "No filename passed, can't find piece image"
        assert (width > 0 and height > 0), "Can't create an invisible piece"
        assert square is not None, "Can't have a piece without a square"
        assert player is not None, "A piece must belong to a player"
        assert (x_position > 0 and x_position < 1200), \
            "Can't create a piece outside the game screen"
        assert (y_position > 0 and y_position < 600), \
            "Can't create a piece outside the game screen"

        super().__init__(x_position, y_position, width, height, filename)
        self.__is_dead = False
        self.__player = player
        self.__square = square

        self.initialize_status()

        self.death_sound = GameSounds("morte.wav")

        # All pieces on game have a option's menu
        self.__menu = PieceMenu.get_piece_menu()

        # All pieces must have an own life bar
        self.__life_bar = LifeBar(self.get_x(), self.get_y(), self.get_health())

    def draw(self, screen, groups):
        groups.add(self.sprite)
        self.__life_bar.draw(screen, groups)
        self.__life_bar.update_life_bar_position(self.get_x(), self.get_y())

    @abstractmethod
    def initialize_status(self):
        pass

    def update(self, event):
        mouse = Mouse()
        # Verify if player is press space to close options' menu
        if(mouse.is_mouse_click(self.get_square(), event)):
            self.__menu.open()
        else:
            # Do nothing
            pass

    def verify_menu_opening(self, event):
        mouse = Mouse()
        if(mouse.is_mouse_click(self, event)):
            self.__menu.open(self)
        else:
            # Do nothing
            pass


    def take_damage(self, life_lost):
        assert(life_lost > 0), "Can't be healed using this method"

        new_health = self.get_health() - life_lost

        if(new_health > 0):
            self.set_health(new_health)
        else:
            self.death_sound.play_sound()
            self.set_health(0)
            self.die()

        self.__life_bar.update_life(self.get_health())


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
        self.__range = rangeAttack

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

    def is_dead(self):
        return self.__is_dead

    def die(self):
        self.__is_dead = True
