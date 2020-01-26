import pygame
import os

class Button:
    def __init__(self, name, img):
        self.name = name
        self.img = img
        self.width = self.img.get_width()
        self.height = self.img.get_height()
        self.x = int
        self.y = int

    def draw(self, window):
        """
        Draw Button
        :param window: surface
        :return: None
        """
        window.blit(self.img, (self.x, self.y))

