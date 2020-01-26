import pygame
import math
import os

class Enemy:
    def __init__(self):
        self.width = 64
        self.height = 64
        self.alive = True
        self.mode = {'hit': 0, 'attack': 1, 'run': 2, 'death': 3}
        self.current_mode = self.mode['run']
        self.imgs_run = []
        self.imgs_death = []
        self.imgs_hit = []
        self.imgs_attack = []
        self.img = None
        self.max_health = 10
        self.health = self.max_health
        self.animation_count = 0
        self.speed = 1
        self.path = [(21, 460), (314, 462), (371, 447), (398, 403), (407, 295), (430, 246), (478, 223), (522, 230), (564, 247), (591, 287), (598, 338), (625, 371), (666, 395), (718, 396), (770, 406), (802, 430), (851, 458), (899, 469), (958, 470), (998, 471)]
        self.path_pos = 0
        self.direction = (0, 0)
        self.x = self.path[0][0]
        self.y = self.path[0][1]

    def animate(self):
        """
        Animate the enemy
        :return: None
        """
        # if mode is run
        if self.current_mode == self.mode['run']:
            self.img = self.imgs_run[self.animation_count]
            self.animation_count += 1
            if self.animation_count >= len(self.imgs_run):
                self.animation_count = 0
        # if mode is death
        elif self.current_mode == self.mode['death']:
            self.img = self.imgs_death[self.animation_count]
            if self.animation_count < len(self.imgs_death):
                self.animation_count += 1
        # if mode is hit
        elif self.current_mode == self.mode['hit']:
            self.img = self.imgs_hit[self.animation_count]
            self.animation_count += 1
            if self.animation_count >= len(self.imgs_hit):
                self.animation_count = 0
                self.current_mode = self.mode['run']

    def draw(self, window):
        """
        Draws the enemy
        :param window: surface
        :return: None
        """
        if self.alive or (not self.alive and self.animation_count == len(self.imgs_death)):
            window.blit(self.img, (self.x - self.width/2, self.y - self.height/2))
            self.draw_health_bar(window)


    def draw_health_bar(self, window):
        """
        Draw Health bar
        :param window: surface
        :return: None
        """
        length = 40
        move_by = round(length / self.max_health)
        health_bar = move_by * self.health

        pygame.draw.rect(window, (255, 0, 0), (self.x - 30, self.y - 40, length, 5), 0)
        pygame.draw.rect(window, (0, 255, 0), (self.x - 30, self.y - 40, health_bar, 5), 0)

    def collide(self, x: int, y: int):
        """
        Returns if position hit enemy
        :param x: int
        :param y: int
        :return: bool
        """
        if self.x + self.width/2 >= x >= self.x - self.width/2:
            if self.y + self.height/2 >= y >= self.y - self.height/2:
                return True
        return False

    def move(self):
        """
        Move the enemy
        :return: None
        """
        if self.alive:
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

    def hit(self, damage: int):
        """
        Returns if an enemy has died and removes one health
        each call
        :param damage: int
        :return: bool
        """
        self.health -= damage

        if self.health <= 0:
            self.health = 0
            self.alive = False
            self.current_mode = self.mode['death']
            self.animation_count = 0
            return True
        else:
            self.current_mode = self.mode['hit']
            self.animation_count = 0
            return True

        return False

    def update(self):
        self.animate()
        self.move()