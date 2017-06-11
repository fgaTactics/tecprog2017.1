import logging
from gameEngine.Scene import *
from gameEngine.GameObject import *
from gameEngine.Mouse import *
from gameEngine.GameEngine import *
from game.PlayerService import *
from gameEngine.GameText import *
from gameEngine.GameSounds import *

# Sprite file names
BACKGROUND_IMAGE = "background.png"
AEROSPACE_IMAGE = "aerospace_class.png"
AUTOMOTIVE_IMAGE = "automotive_class.png"
ELETRONIC_IMAGE = "eletronic_class.png"
ENERGY_IMAGE = "energy_class.png"
SOFTWARE_IMAGE = "software_class.png"

# All the following constants are pixels units
IMAGE_WIDTH = 150
IMAGE_HEIGHT = 150

# Background measurements
BACKGROUND_POS_X = 0
BACKGROUND_POS_Y = 0
BACKGROUND_WIDTH = 1199
BACKGROUND_HEIGHT = 600

# Constants to define class' image position on screen
POSITION_X_AEROSPACE = 230
POSITION_X_AUTOMOTIVE = 530
POSITION_X_ELETRONIC = 830
POSITION_X_ENERGY = 370
POSITION_X_SOFTWARE = 670

POSITION_Y_AEROSPACE = 100
POSITION_Y_AUTOMOTIVE = 100
POSITION_Y_ELETRONIC = 100
POSITION_Y_ENERGY = 370
POSITION_Y_SOFTWARE = 370


# Select the class wich the player wants to fight for
class ClassSelectionScene(Scene):

    def __init__(self, name="DEFAULT", ID=0):
        super().__init__(name, ID)

        self.background = GameObject(BACKGROUND_POS_X,
                                     BACKGROUND_POS_Y,
                                     BACKGROUND_WIDTH,
                                     BACKGROUND_HEIGHT,
                                     BACKGROUND_IMAGE)

        self.class_aerospace = GameObject(POSITION_X_AEROSPACE,
                                          POSITION_Y_AEROSPACE,
                                          IMAGE_WIDTH,
                                          IMAGE_HEIGHT,
                                          AEROSPACE_IMAGE)

        self.class_automotive = GameObject(POSITION_X_AUTOMOTIVE,
                                           POSITION_Y_AUTOMOTIVE,
                                           IMAGE_WIDTH,
                                           IMAGE_HEIGHT,
                                           AUTOMOTIVE_IMAGE)

        self.class_eletronic = GameObject(POSITION_X_ELETRONIC,
                                          POSITION_Y_ELETRONIC,
                                          IMAGE_WIDTH,
                                          IMAGE_HEIGHT,
                                          ELETRONIC_IMAGE)

        self.class_energy = GameObject(POSITION_X_ENERGY,
                                       POSITION_Y_ENERGY,
                                       IMAGE_WIDTH,
                                       IMAGE_HEIGHT,
                                       ENERGY_IMAGE)

        self.class_software = GameObject(POSITION_X_SOFTWARE,
                                         POSITION_Y_SOFTWARE,
                                         IMAGE_WIDTH,
                                         IMAGE_HEIGHT,
                                         SOFTWARE_IMAGE)

        self.sound_button = GameSounds("")

        # Initialize attribute
        self.number_of_clicks = 0

    def update(self, event):
        mouse = Mouse()

        player_class = None

        # Check where player click to select class
        if (mouse.is_mouse_click(self.class_aerospace, event)):
            logging.info("Você escolheu Aeroespacial!")
            self.sound_button.play_sound()
            player_class = "aerospace"
            self.number_of_clicks = self.number_of_clicks + 1

        elif (mouse.is_mouse_click(self.class_automotive, event)):
            logging.info("Você escolheu Automotiva!")
            self.sound_button.play_sound()
            player_class = "automotive"
            self.number_of_clicks = self.number_of_clicks + 1

        elif (mouse.is_mouse_click(self.class_eletronic, event)):
            logging.info("Você escolheu Eletrônica!")
            self.sound_button.play_sound()
            player_class = "eletronic"
            self.number_of_clicks = self.number_of_clicks + 1

        elif (mouse.is_mouse_click(self.class_energy, event)):
            logging.info("Você escolheu Energia!")
            self.sound_button.play_sound()
            player_class = "energy"
            self.number_of_clicks = self.number_of_clicks + 1

        elif (mouse.is_mouse_click(self.class_software, event)):
            logging.info("Você escolheu Software!")
            self.sound_button.play_sound()
            player_class = "software"
            self.number_of_clicks = self.number_of_clicks + 1
        else:
            # Nothing to do
            pass

        if(player_class is None):
            # Do nothing
            pass
        else:
            if(self.number_of_clicks == 1):
                self.player1_class = player_class
            else:
                self.player2_class = player_class
            player_class = None

        if (self.number_of_clicks >= 2):
            logging.debug("Os dois jogadores selecionaram as classes ! Trocando cena")
            PlayerService.set_player(self.player1_class, 0)
            PlayerService.set_player(self.player2_class, 1)

            gameEngine = GameEngine.get_instance()
            gameEngine.scene_manager.load_next_scene()

    def draw(self, screen, groups):
        groups.add(self.background.sprite)

        if(self.number_of_clicks == 0):
            GameText.print("Selecione a classe do Jogador 1", 400, 25)
        else:
            GameText.print("Selecione a classe do Jogador 2", 400, 25)

        groups.add(self.class_aerospace.sprite)
        groups.add(self.class_automotive.sprite)
        groups.add(self.class_eletronic.sprite)
        groups.add(self.class_energy.sprite)
        groups.add(self.class_software.sprite)

        GameText.print("Aerospacial", 225, 265)
        GameText.print("Automotiva", 527, 265)
        GameText.print("Eletronica", 837, 265)
        GameText.print("Energia", 393, 535)
        GameText.print("Software", 689, 535)
