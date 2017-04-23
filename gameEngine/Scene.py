
"""This class created the basic
structure for scene
"""
import pygame


class Scene(object):


    def __init__(self, name="DEFAULT", ID=0):
        self.name = name
        self.ID = ID

    def update(self):
        pass

    def draw(self, groups):
        pass
