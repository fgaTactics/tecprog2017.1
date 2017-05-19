# -- This class is responsable for draw the board at the screen -- #

import pygame
from gameEngine.GameObject import *
from game.gameboard.Square import *
from game.pieces.FreshMan import *

# RGB color definitions
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)


class GameBoard:
    # PARÂMETROS DE ENTRADA MUDAM (receber o número de colunas e linhas?)

    # Grid with all positions of squares at the board
    grid = []

    # Spacing in pixels between the board and the edges of the screen
    lateral_spacing = 217
    top_spacing = 180

    # Amount of rows and columns of the board
    amount_of_rows = 5
    amount_of_columns = 10

    # Positions in pixels of ending of the board
    end_position = (982, 555)

    # Square size of the board and margin size between them
    square_size = 60
    square_margin = 15


    def __init__(self, game_board_square_size=0):
        self.board_width = game_board_square_size
        self.board_height = game_board_square_size

        # Add all square positions
        for row in range(self.amount_of_rows):
            self.grid.append([])
            for column in range(self.amount_of_columns):
                self.grid[row].append(Square(0, 0))
                # calcular x e y automaticamente
        # print(self.grid[0][0].has_piece())
        # piece = FreshMan(0,0,0,0,0,0,"","",0,0,0,0,"logo.png")
        # self.grid[0][0].add_piece(piece)
        # print(self.grid[0][0].has_piece())
    # colocar uma peça
    # remover uma peça
    # mover uma peça

    def draw(self, screen):
        # Draw all the squares that form the board
        for row in range(self.amount_of_rows):
            for column in range(self.amount_of_columns):
                color = WHITE

                pygame.draw.rect(screen,
                                 color,
                                 [self.lateral_spacing +
                                  (self.square_margin + self.board_width) *
                                  column + self.square_margin,
                                  self.top_spacing +
                                  (self.square_margin + self.board_height) *
                                  row + self.square_margin,
                                  self.board_width,
                                  self.board_height])
