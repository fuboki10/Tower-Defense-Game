import pygame
import os
from .enemy import Enemy

imgs_run = []
for i in range(24):
    add_str = str(i)
    if i < 10:
        add_str = "0" + add_str
    imgs_run.append(pygame.transform.scale(
        pygame.image.load(os.path.join("assets/enemies/1/Run", "Version1_Run_" + add_str + ".png")),
        (64, 64)))

imgs_death = []
for i in range(24):
    add_str = str(i)
    if i < 10:
        add_str = "0" + add_str
    imgs_death.append(pygame.transform.scale(
        pygame.image.load(os.path.join("assets/enemies/1/Death2", "Version1_Death2_" + add_str + ".png")),
        (64, 64)))


class Bat(Enemy):
    def __init__(self):
        super().__init__()
        self.name = "bat"
        self.max_health = 10
        self.health = self.max_health
        self.imgs_run = imgs_run[:]
        self.imgs_death = imgs_death[:]
