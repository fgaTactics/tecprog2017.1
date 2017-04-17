import pygame
from gameEngine.GameObject import *

# Define some colors
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)


class GameBoard:
    # Grid for draw board game
    grid = []
    lateralSpaceRow = 180
    lateralSpaceColumn = 240

    def __init__(self, width=0, height=0, margin=0):
        self.width = width
        self.height = height
        self.margin = margin

        for row in range(5):
            # Add an empty array that will hold each cell
            self.grid.append([])
            for column in range(10):
                self.grid[row].append(0)

    def draw(self, screen):
        # Create matriz board for the game
        for row in range(5):
            for column in range(10):
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
