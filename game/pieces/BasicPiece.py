from pygame import *
from gameEngine.GameObject import GameObject
from gameEngine.Mouse import *
from game.gameboard.PieceMenu import *

"""This class is a model for the game pieces"""


class BasicPiece(GameObject):

    # All pieces on game have a option's menu
    menu = PieceMenu()

    def __init__(self, health=0, attack=0, rangeAttack=0, defense=0,
                 amount_of_moviment=0, penalty=0,
                 hability="", description="", x_position=0, y_position=0, width=0,
                 height=0, filename=""):
        super().__init__(x_position, y_position, width, height, filename)
        self.set_health(health)
        self.set_attack(attack)
        self.set_defense(defense)
        self.set_amount_of_moviment(amount_of_moviment)
        self.set_penalty(penalty)
        self.set_hability(hability)
        self.set_description(description)
        self.menu_is_open = False

    def draw(self, screen, groups):
        groups.add(self.sprite)

        # Verify is player is click in any piece to open option's menu
        if(self.menu_is_open):
            print("Menu da peça foi aberto ! Selecione as opções")

            # Set menu positions relative to piece
            self.menu.set_positions(self)
            self.menu.is_open = True
            self.menu.draw(screen, groups)
        else:
            # Nothing to do
            pass

    def update(self, event):
        mouse = Mouse()
        # Verify if player is press space to close options' menu
        if(mouse.is_mouse_click(self, event)):
            self.menu_is_open = True

        if(event.type == pygame.KEYDOWN):
            if event.key == K_SPACE:
                self.menu_is_open = False
                self.menu.is_open = False
        else:
            # Nothing to do
            pass

    def get_health(self):
        return self.__health

    def set_health(self, health):
        self.__health = health

    def get_attack(self):
        return self.__attack

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
