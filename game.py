import pygame
import os
from enemies.bat import Bat

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
            self.input()
            self.update()
            self.draw()

        pygame.quit()

    def input(self):
        """
        Handle user input
        :return: None
        """

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

            pos = pygame.mouse.get_pos()

            if event.type == pygame.MOUSEBUTTONDOWN:
                self.clicks.append(pos)
                # print(self.clicks)
                for enemy in self.enemies:
                    if enemy.collide(pos[0], pos[1]):
                        enemy.hit(1)

    def update(self):
        """
        updates the Game
        :return: None
        """
        self.delete_dead_enemies()

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
        self.enemies.append(Bat())

    def delete_dead_enemies(self):
        """
        Delete Dead Enemies
        :return: None
        """
        to_delete = []
        for enemy in self.enemies:
            if enemy.alive == False and enemy.animation_count >= len(enemy.imgs_death):
                to_delete.append(enemy)

        for d in to_delete:
            self.enemies.remove(d)

g = Game(1000, 700)
g.run()