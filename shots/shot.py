import pygame
import math

class Shot:
    def __init__(self, x, y, target):
        self.x = x
        self.y = y
        self.target = target
        self.imgs = []
        self.animation_count = 0
        self.timer = 0
        self.speed = 3
        self.damage = 1
        self.mode = {'attack': 0, 'stop': 1, 'boom': 2}
        self.current_mode = self.mode['stop']

    def draw(self, window):
        """
        Draws the Shot
        :param window: Surface
        :return: None
        """
        img = self.imgs[self.animation_count]

        window.blit(img, (self.x - img.get_width() / 2, self.y - img.get_height() / 2))

    def move(self, x=0, y=0):
        """
        Move the Shot
        :return: None
        """
        dis = math.sqrt((self.x - self.target[0]) ** 2 + (self.y - self.target[1]) ** 2)
        if dis <= self.speed and self.current_mode == self.mode['attack']:
            self.current_mode = self.mode['boom']

        if self.current_mode == self.mode['stop']:
            self.x = x
            self.y = y
        elif self.current_mode == self.mode['attack']:
            direction = math.atan2(self.target[1] - self.y, self.target[0] - self.x) * (180 / math.pi)
            mv_x = math.cos(direction * math.pi / 180) * self.speed
            mv_y = math.sin(direction * math.pi / 180) * self.speed
            self.x += mv_x
            self.y += mv_y
        elif self.current_mode == self.mode['boom']:
            self.animation_count += 1
            if self.animation_count >= len(self.imgs):
                self.animation_count = 0
                self.current_mode = self.mode['stop']

    def attack(self, target):
        self.target = target
        self.current_mode = self.mode['attack']
