from gameEngine.Scene import *
from game.gameboard.GameBoard import *
from game.gameboard.PieceList import *
from game.PlayerService import *
from gameEngine.Mouse import *


class ArmyPositioningScene(Scene):

    def __init__(self, name="DEFAULT", ID=0):
        super().__init__(name, ID)
        self.game_board = GameBoard(60, 60)
        self.player1_first_confirm = 0
        self.player1_second_confirm = 0
        self.player2_confirm = 0

        self.confirm_button = GameObject(500, 150, 150,
                                         150,
                                         "start_button.png")

    def load(self):
        player1_class = PlayerService.get_player(0)
        player2_class = PlayerService.get_player(1)
        self.left_piece_list = PieceList(player1_class, 0, 0, 200, 800, "PieceMenu.png")
        self.right_piece_list = PieceList(player2_class, 1000, 0, 200, 800,
                                          "PieceMenu.png")


    def draw(self, screen, groups):
        screen.fill((0, 0, 0))
        self.game_board.draw(screen)
        self.left_piece_list.draw(screen, groups)
        self.right_piece_list.draw(screen, groups)
        text_x_position = 400
        text_y_position = 100

        self.show_confirm_button(screen, groups)

        if(self.player1_first_confirm == 0):
            GameText.print("Player 1: Select your Pieces",
                           text_x_position, text_y_position)
        elif(self.player2_confirm == 0):
            GameText.print("Player 2: Select your Pieces",
                           text_x_position, text_y_position)
        elif(self.player2_confirm == 1):
            GameText.print("Player 1: Select your remaining Pieces",
                           text_x_position, text_y_position)

    def show_confirm_button(self, screen, groups):
        if(self.player1_first_confirm == 0 and
           self.left_piece_list.count_pieces_in_board() >= 5):
            groups.add(self.confirm_button.sprite)
        elif(self.player2_confirm == 0 and
             self.right_piece_list.count_pieces_in_board() >= 10):
            groups.add(self.confirm_button.sprite)
        elif(self.player1_second_confirm == 0 and
             self.left_piece_list.count_pieces_in_board() >= 10):
            groups.add(self.confirm_button.sprite)

    def update(self, event):
        if(self.player1_first_confirm == 0):
            self.left_piece_list.update(event)
        elif(self.player2_confirm == 0):
            self.right_piece_list.update(event)
        elif(self.player2_confirm == 1):
            self.left_piece_list.update(event)

        self.verify_player_confirmation()

    def verify_player_confirmation(self):
        mouse = Mouse()

        if(self.player1_first_confirm == 0 and
           self.left_piece_list.count_pieces_in_board() >= 5):
            DraggablePiece.set_drag_enable(False)
            if(mouse.is_mouse_click(self.confirm_button)):
                self.player1_first_confirm = 1
        elif(self.player2_confirm == 0 and
             self.right_piece_list.count_pieces_in_board() >= 10):
            DraggablePiece.set_drag_enable(False)
            if(mouse.is_mouse_click(self.confirm_button)):
                self.player2_confirm = 1
        elif(self.player1_second_confirm == 0 and
             self.left_piece_list.count_pieces_in_board() >= 10):
            DraggablePiece.set_drag_enable(False)
            if(mouse.is_mouse_click(self.confirm_button)):
                self.player1_second_confirm = 1
        else:
            DraggablePiece.set_drag_enable(True)
