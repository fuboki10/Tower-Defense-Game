import pygame
import os
import time
import random
from enemies.bat import Bat

pygame.font.init()

hearts_img = pygame.image.load(os.path.join("assets", "hearts@3x.png"))
coins_img = pygame.image.load(os.path.join("assets", "coins@3x.png"))

class Game:
    def __init__(self, window, width, height):
        """
        :param width: INT
        :param height: INT
        """
        self.width = width
        self.height = height
        self.window = window
        self.enemies = []
        self.towers = []
        self.lives = 10
        self.money = 100
        self.timer = time.time()
        self.font = pygame.font.SysFont("comicsans", 30)
        self.bg = pygame.image.load(os.path.join("assets", "lvl1.jpg"))
        self.bg = pygame.transform.scale(self.bg, (self.width, self.height))
        self.running = False
        self.app_running = True
        self.clicks = []

        self.gen_enemies()

    def run(self):
        """
        Running the Game
        Returns True if the Application is closed else False
        :return: bool
        """
        self.running = True
        clock = pygame.time.Clock()

        while self.running:
            clock.tick(60)
            self.input()
            self.update()
            self.draw()
        return self.app_running

    def input(self):
        """
        Handle user input
        :return: None
        """

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
                self.app_running = False

            pos = pygame.mouse.get_pos()

            if event.type == pygame.MOUSEBUTTONDOWN:
                self.clicks.append(pos)
                # print(self.clicks)
                for enemy in self.enemies:
                    if enemy.collide(pos[0], pos[1]) and enemy.alive == True:
                        enemy.hit(1)

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.running = False

    def update(self):
        """
        updates the Game
        :return: None
        """
        self.delete_dead_enemies()
        if time.time() - self.timer >= random.randrange(2,6):
            self.timer = time.time()
            self.gen_enemies()

    def draw(self):
        """
        Draw Game
        :return: None
        """
        self.window.blit(self.bg, (0, 0))
        for p in self.clicks:
            pygame.draw.circle(self.window, (255, 0, 0), (p[0], p[1]), 5, 0)

        # Draw Enemies
        for enemy in self.enemies:
            enemy.draw(self.window)

        # draw lives
        text = self.font.render(str(self.lives), 1, (76, 28, 18))
        start_x = self.width - hearts_img.get_width() - 10

        self.window.blit(hearts_img, (start_x, 10))
        self.window.blit(text, (start_x + hearts_img.get_width()/2, 20))

        # draw money
        text = self.font.render(str(self.money), 1, (76, 28, 18))
        start_x = self.width - coins_img.get_width() - 10

        self.window.blit(coins_img, (start_x, 65))
        self.window.blit(text, (start_x + coins_img.get_width()/2 - 10, 80))

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
            self.money += d.money
            self.enemies.remove(d)
