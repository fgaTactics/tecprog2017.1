
import pygame

from sys import exit


class GameLoop:
    __height = 0
    __weidht = 0

    def __init__(self, height, weidht):
        self.__height = height
        self.__weidh = weidht
    
    
    def startScreen(self, height, weidht, windowsName):
        screen = pygame.display.set_mode((height,weidht))
        pygame.display.set_caption(windowsName)
        
    
    def gameLoopStart(self , height,weight):
        
        pygame.init()
        
        while True:
            self.startScreen(height, weight,'Start Game')
            for event in pygame.event.get():
                
                if(event.type == pygame.QUIT):
                    exit()
                
                else:
                    #do nothing
                    
                    pygame.display.update()
            
                    
        