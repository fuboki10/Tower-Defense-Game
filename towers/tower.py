import pygame


class Tower:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.sell_price = [0, 0, 0]
        self.buy_price = [0, 0, 0]
        self.level = 1
        self.imgs = []
        self.damage = 0

    def draw(self, window):
        """
        Draws the Tower
        :param window: surface
        :return: None
        """
        img = self.imgs[self.level - 1]
        window.blit(img, (self.x - img.get_width() / 2, self.y - img.get_height() / 2))

    def move(self, x, y):
        """
        Change Tower Position
        :param x: int
        :param y: int
        :return: None
        """
        self.x = x
        self.y = y
