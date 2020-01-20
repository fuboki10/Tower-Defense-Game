import pygame
import os

logo = pygame.image.load(os.path.join("assets", "logo.png"))

class MainMenu:
    def __init__(self, window, width, height):
        self.width = width
        self.height = height

