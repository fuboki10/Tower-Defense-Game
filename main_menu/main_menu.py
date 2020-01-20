import pygame
import os
from game import Game

logo = pygame.image.load(os.path.join("assets", "logo.png"))
start_button = pygame.image.load(os.path.join("assets/menu", "StartButton.png"))

class MainMenu:
    def __init__(self, window, width: int, height: int):
        """
        :param window: surface
        :param width: int
        :param height: int
        """
        self.width = width
        self.height = height
        self.bg = pygame.image.load(os.path.join("assets", "lvl1.jpg"))
        self.bg = pygame.transform.scale(self.bg, (self.width, self.height))
        self.window = window
        self.button = (self.width/2 - start_button.get_width()/2, 350, start_button.get_width(), start_button.get_height())
        self.running = False

    def run(self):
        """
        Open Main Menu
        :return: None
        """
        self.running = True
        clock = pygame.time.Clock()
        while self.running:
            clock.tick(60)
            self.draw()
            self.input()
        pygame.quit()

    def draw(self):
        self.window.blit(self.bg, (0, 0))
        self.window.blit(logo, (self.width/2 - logo.get_width()/2, 0))
        self.window.blit(start_button, (self.button[0], self.button[1]))
        pygame.display.update()

    def input(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()

                if self.button[0] <= x <= self.button[0] + self.button[2]:
                    if self.button[1] <= y <= self.button[1] + self.button[3]:
                        game = Game(self.window, self.width, self.height)
                        self.running = game.run()
                        del game

