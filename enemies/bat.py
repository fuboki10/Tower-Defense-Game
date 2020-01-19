import pygame
import os
from .enemy import Enemy

imgs = []
for i in range(24):
    add_str = str(i)
    if i < 10:
        add_str = "0" + add_str
    imgs.append(pygame.transform.scale(
        pygame.image.load(os.path.join("assets/enemies/1/Run", "Version1_Run_" + add_str + ".png")),
        (64, 64)))


class Bat(Enemy):
    def __init__(self):
        super().__init__()
        self.name = "bat"
        self.max_health = 10
        self.health = self.max_health
        self.imgs = imgs[:]
