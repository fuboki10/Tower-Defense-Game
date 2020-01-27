import pygame
import os
from .shot import Shot

imgs = []

for i in range(6):
    img = pygame.image.load(os.path.join("assets/shots/1/", str(i) + ".png"))
    imgs.append(pygame.transform.scale(img, (img.get_width() // 2, img.get_height() // 2)))


class Stone(Shot):
    def __init__(self, x, y, target):
        super().__init__(x, y, target)
        self.imgs = imgs[:]

