from gameEngine.GameObject import *
import math

# Refactor
LATERAL_SPACE_ROW = 10
LATERAL_SPACE_COLUMN = 240

class DraggablePiece(GameObject):

    isDrag = False
    mouse_position = [0, 0]
    corners = []
    
    def __init__(self, x_position, y_position, width, height, filename):
        
        # Refactor
        for x in range(LATERAL_SPACE_COLUMN, 375, 75):
            for y in range(LATERAL_SPACE_ROW, 750, 75):
                self.corners.append((x,y)) 
                
        super().__init__(x_position, y_position, width, height, filename)        
        

    def update(self, event):
        self.drag(event)

    """" Verify if the piece is being draged on the screen
         and change the piece position """
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
            # Refactor
            px, py = self.sprite.rect.topleft
            for cx, cy in self.corners:
                # Refactor
                if math.hypot(cx-px, cy-py) < 40:
                    self.set_x(cx+20)
                    self.set_y(cy+20)
                    break                      
