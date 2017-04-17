from gameEngine.GameObject import *
from gameboard.GameBoard import *
import math

SIDE_OF_THE_SQUARE = 75
BEGINNING_OF_THE_BOARD = 375
END_OF_THE_BOARD = 750

class DraggablePiece(GameObject):

    isDrag = False
    mousePosition = [0, 0]
    corners = []
    
    def __init__(self, x_position, y_position, width, height, filename):
        
        #Define the board space
        for x in range(GameBoard.lateralSpaceColumn, BEGINNING_OF_THE_BOARD, SIDE_OF_THE_SQUARE):
            for y in range(GameBoard.lateralSpaceRow, END_OF_THE_BOARD, SIDE_OF_THE_SQUARE):
                self.corners.append((x,y))
                
        super().__init__(x_position, y_position, width, height, filename)        
        

    def update(self, event):
        self.drag(event)

    #Verify if the piece is being draged on the screen
    #and change the piece position
    def drag(self, event):
    
        if(event.type == pygame.MOUSEBUTTONDOWN):
            self.mouse_position = pygame.mouse.get_pos()
            if(self.sprite.rect.collidepoint(self.mouse_position[0],
                                             self.mouse_position[1])):
                self.isDrag = True
        elif(event.type == pygame.MOUSEBUTTONUP):
            self.isDrag = False

        if(self.isDrag):            
            self.mouse_position = pygame.mouse.get_pos()
            self.set_x(self.mouse_position[0] - self.width / 2)
            self.set_y(self.mouse_position[1] - self.height / 2)
        else:
            OBJECT_POSITION_X, OBJECT_POSITION_Y = self.sprite.rect.topleft
            for BOARD_POSITION_X, BOARD_POSITION_Y in self.corners:
                if math.hypot(BOARD_POSITION_X-OBJECT_POSITION_X, 
                              BOARD_POSITION_Y-OBJECT_POSITION_Y) < 40:
                    self.set_x(BOARD_POSITION_X+20)
                    self.set_y(BOARD_POSITION_Y+20)
                    break                      
