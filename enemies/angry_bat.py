import pygame
import os
from .enemy import Enemy

imgs_run = []
for i in range(24):
    add_str = str(i)
    if i < 10:
        add_str = "0" + add_str
    imgs_run.append(pygame.transform.scale(
        pygame.image.load(os.path.join("assets/enemies/2/Run", "Version1_Run_" + add_str + ".png")),
        (64, 64)))

imgs_death = []
for i in range(24):
    add_str = str(i)
    if i < 10:
        add_str = "0" + add_str
    imgs_death.append(pygame.transform.scale(
        pygame.image.load(os.path.join("assets/enemies/2/Death2", "Version1_Death2_" + add_str + ".png")),
        (64, 64)))


class AngryBat(Enemy):
    def __init__(self):
        super().__init__()
        self.name = "angry_bat"
        self.max_health = 15
        self.health = self.max_health
        self.money = 2
        self.imgs_run = imgs_run[:]
        self.imgs_death = imgs_death[:]
        self.damage = 2
