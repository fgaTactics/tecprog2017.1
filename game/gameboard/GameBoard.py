import pygame
from gameEngine.GameObject import *

# Define some colors
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
LATERAL_SPACE_ROW = 180
LATERAL_SPACE_COLUMN = 240


class GameBoard:
    # Grid for draw board game
    grid = []

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
                if self.grid[row][column] == 1:
                    color = GREEN
                else:
                    # Do nothing
                    pass

                pygame.draw.rect(screen,
                                 color,
                                 [LATERAL_SPACE_COLUMN +
                                  (self.margin + self.width) *
                                  column + self.margin,
                                  LATERAL_SPACE_ROW +
                                  (self.margin + self.height) *
                                  row + self.margin,
                                  self.width,
                                  self.height])

    def update(self, event):

        if event.type == pygame.MOUSEBUTTONDOWN:
                # User clicks the mouse. Get the position
                position = pygame.mouse.get_pos()
                # Change the x/y screen coordinates to grid coordinates
                column = position[0] // (self.width +
                                         self.margin)
                row = position[1] // (self.height +
                                      self.margin)
                self.grid[row][column] = 1
                print("Click ", position, "Grid coordinates: ", row, column)
