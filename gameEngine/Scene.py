import pygame

# This class creates the scene basic structure


class Scene(object):

    def __init__(self, name="DEFAULT", ID=0):
        self.name = name
        self.ID = ID

    def update(self, events):
        pass

    def load(self):
        pass

    def draw(self, screen, groups):
        pass
