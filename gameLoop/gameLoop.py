
import pygame
class GameLoop :
    __height
    __weidht
    
    def __init__(self , height,weidht):
        self.__height = height
        self.__weidh = weidh
    
    
    def startScreen(self , height , weidht):
        screen = pygame.display.set_mode(height,weidht)
        pygame.display.set_caption("teste")
        
    
    def gameLoopStart(self , height,weight):
        pygame.init()        
        while True :
            startScreem(height,weight)
            for start in pygame.event.get():
                if(start.type == QUIT):
                    pygame.quit()
                    sys.exit()
                    
            pygame.display.update()
            
                    
        