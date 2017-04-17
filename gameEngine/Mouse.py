import pygame


class Mouse:

    def __init__(self):
        self.position = pygame.mouse.get_pos()
        self.click = pygame.mouse.get_pressed()

    def is_mouse_over(self, element):

        if((element.get_x() + element.width > self.position[0] > element.get_x()) and
           (element.get_y() + element.height > self.position[1] > element.get_y())):
            return True
        else:
            return False

    def is_mouse_click(self, element):

        if(self.is_mouse_over(element) and self.click[0]):
            return True
        else:
            return False
