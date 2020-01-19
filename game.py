import pygame
import os
from enemies.enemy import Enemy

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
        self.clicks = []

        self.gen_enemies()

    def run(self):
        self.running = True
        clock = pygame.time.Clock()

        while self.running:
            clock.tick(60)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

                pos = pygame.mouse.get_pos()

                if event.type == pygame.MOUSEBUTTONDOWN:
                    self.clicks.append(pos)
                    print(self.clicks)

            self.draw()

        pygame.quit()


    def draw(self):
        """
        Draw Game
        :return: None
        """
        self.window.blit(self.bg, (0, 0))
        for p in self.clicks:
            pygame.draw.circle(self.window, (255, 0, 0), (p[0], p[1]), 5, 0)

        for enemy in self.enemies:
            enemy.draw(self.window)
        pygame.display.update()

    def gen_enemies(self):
        """
        Generate enemies
        :return: None
        """
        self.enemies.append(Enemy())

g = Game(1000, 700)
g.run()