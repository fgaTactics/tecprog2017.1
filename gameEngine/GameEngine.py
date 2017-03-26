
import pygame
from gameEngine.GameCanvas import *

from sys import exit


class GameEngine:

    def run(self):
        pygame.init()
        
        while True:
            
            canvas = GameCanvas(800,600)
            canvas.startScreen()
            
            for event in pygame.event.get():
                
                if(event.type == pygame.QUIT):
                    exit()
                
                else:
                    #do nothing
                    
                    pygame.display.update()
            
                    
        