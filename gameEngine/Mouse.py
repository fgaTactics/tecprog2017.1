import pygame

# This class controls all mouse functionalities


class Mouse:

    def __init__(self):
        self.position = pygame.mouse.get_pos()
        self.click = pygame.mouse.get_pressed()

    def is_mouse_over(self, element):
        if((element.get_x() + element.get_width() > self.position[0] > element.get_x()) and
           (element.get_y() + element.get_height() > self.position[1] > element.get_y())):
            return True
        else:
            return False

    def is_mouse_click(self, element, event):
        if(self.is_mouse_over(element)):
            if(event.type == pygame.MOUSEBUTTONUP):
                return True
            else:
                return False
        else:
            return False

    def is_mouse_not_click(self, element):
        if(self.is_mouse_over(element) and self.click[0]):
            return False
        else:
            return True
