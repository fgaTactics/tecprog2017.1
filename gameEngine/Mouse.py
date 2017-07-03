import pygame

# This class controls all mouse functionalities


class Mouse:

    def __init__(self):
        # Array with mouse x and y positions
        self.position = pygame.mouse.get_pos()
        assert (self.position is not None), "Invalid pygame mouse position return"

        # Array that indicate if some mouse button is pressed
        self.click = pygame.mouse.get_pressed()
        assert (self.click is not None), "Invalid pygame mouse click return"

    # Verify if mouse cursor is over a certain object
    def is_mouse_over(self, element):

        # Compare object coordinates with mouse position
        if((element.get_x() + element.get_width() > self.position[0] >
            element.get_x()) and (element.get_y() + element.get_height() >
                                  self.position[1] > element.get_y())):
            return True
        else:
            return False

    # Verify if the mouse cursor was over a certain object during a click event
    def is_mouse_click(self, element, event):

        # Verify coincidence between mouse cursor and object position
        if(self.is_mouse_over(element)):

            # Watch the mouse button release after a click
            if(event.type == pygame.MOUSEBUTTONUP):
                return True
            else:
                return False
        else:
            return False
