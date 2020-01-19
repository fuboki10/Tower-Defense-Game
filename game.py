import pygame
import os

class Game:
    def __init__(self, width, height):
        """
        :param width: INT
        :param height: INT
        """
        self.width = width
        self.height = height
        self.window = pygame.display.set_mode((self.width, self.height))
        self.enemies = []
        self.towers = []
        self.lives = 10
        self.money = 100
        self.bg = pygame.image.load(os.path.join("assets", "lvl1.jpg"))
        self.bg = pygame.transform.scale(self.bg, (self.width, self.height))
        self.running = False


    def run(self):
        self.running = True
        clock = pygame.time.Clock()
        while self.running:
            clock.tick(60)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

        pygame.quit()

    def draw(self):
        """
        Draw Game
        :return: None
        """
        self.window.blit(self.bg, (0, 0))
        pygame.display.update()