import pygame
from gameEngine.GameObject import *

# Define some colors
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
AMOUNT_OF_ROW = 5
AMOUNT_OF_COLUMN = 10


class GameBoard:
    # Grid for draw board game
    grid = []
    lateralSpaceRow = 180
    lateralSpaceColumn = 217

    def __init__(self, width=0, height=0, margin=0):
        self.width = width
        self.height = height
        self.margin = margin

        for row in range(AMOUNT_OF_ROW):
            # Add an empty array that will hold each cell
            self.grid.append([])
            for column in range(AMOUNT_OF_COLUMN):
                self.grid[row].append(0)

    def draw(self, screen):
        # Create matriz board for the game
        for row in range(AMOUNT_OF_ROW):
            for column in range(AMOUNT_OF_COLUMN):
                color = WHITE

                pygame.draw.rect(screen,
                                 color,
                                 [GameBoard.lateralSpaceColumn +
                                  (self.margin + self.width) *
                                  column + self.margin,
                                  GameBoard.lateralSpaceRow +
                                  (self.margin + self.height) *
                                  row + self.margin,
                                  self.width,
                                  self.height])
