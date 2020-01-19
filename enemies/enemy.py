import pygame
import math
import os

class Enemy:
    def __init__(self):
        self.width = 20
        self.health = 20
        self.imgs = [pygame.image.load(os.path.join("assets", "bl-1-Monster No001-1.png")).convert_alpha()]
        self.img = None
        self.health = 0
        self.animation_count = 0
        self.speed = 1
        self.path = [(21, 460), (314, 462), (371, 447), (398, 403), (407, 295), (430, 246), (478, 223), (522, 230), (564, 247), (591, 287), (598, 338), (625, 371), (666, 395), (718, 396), (770, 406), (802, 430), (851, 458), (899, 469), (958, 470), (998, 471)]
        self.path_pos = 0
        self.direction = (0, 0)
        self.x = self.path[0][0]
        self.y = self.path[0][1]

    def draw(self, window):
        """
        Draws the enemy
        :param window: surface
        :return: None
        """
        self.img = self.imgs[self.animation_count]
        self.animation_count += 1
        if self.animation_count >= len(self.imgs):
            self.animation_count = 0
        window.blit(self.img, (self.x - self.img.get_width()/2, self.y - self.img.get_height()/2 - 35))
        self.move()

    def collide(self, x, y):
        """
        Returns if position hit enemy
        :param x: int
        :param y: int
        :return: bool
        """
        if self.x + self.width >= x >= self.x:
            if self.y + self.height >= y >= self.y:
                return True
        return False

    def move(self):
        """
        Move enemy
        :return: None
        """

        x1, y1 = self.path[self.path_pos]
        if self.path_pos + 1 >= len(self.path):
            x2, y2 = x1, y1
        else:
            x2, y2 = self.path[self.path_pos + 1]

        mag = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
        if mag != 0:
            self.direction = ((x2 - x1) / mag, (y2 - y1) / mag)
            self.x += self.direction[0] * self.speed
            self.y += self.direction[1] * self.speed
            if (self.x, self.y) >= self.path[self.path_pos + 1]:
                self.path_pos += 1

    def hit(self, damage):
        """
        Returns if an enemy has died and removes one health
        each call
        :param damage: int
        :return: bool
        """
        self.health -= damage
        if self.health <= 0:
            return True
        return False
