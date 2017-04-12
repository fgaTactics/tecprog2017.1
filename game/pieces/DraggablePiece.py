from gameEngine.GameObject import *

class DraggablePiece(GameObject):

    isDrag = False
    mouse_position = [0, 0]

    def update(self, event):
        self.drag(event)


    """" Verify if the piece is being draged on the screen
         and change the piece position """
    def drag(self, event):   
        if(event.type == pygame.MOUSEBUTTONDOWN):
            self.mouse_position = pygame.mouse.get_pos()
            if(self.sprite.rect.collidepoint(self.mouse_position[0], self.mouse_position[1])):
                self.isDrag = True
        elif(event.type == pygame.MOUSEBUTTONUP):
            self.isDrag = False
            
        if(self.isDrag):
            self.mouse_position = pygame.mouse.get_pos()
            self.set_x(self.mouse_position[0] - self.width / 2)
            self.set_y(self.mouse_position[1] - self.height / 2)
