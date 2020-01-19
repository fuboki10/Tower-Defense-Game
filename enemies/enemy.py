import pygame

class Enemy:
    def __init__(self, x, y, width, height):
        """
        :param width: int
        :param height: int
        :param x: int
        :param y: int
        """
        self.x = x
        self.y = y
        self.width = width
        self.health = height
        self.imgs = []
        self.img = None
        self.health = 0
        self.animation_count = 0
        self.speed = 1
        self.path = []

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
        window.blit(self.img, (self.x, self.y))

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
        pass

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
