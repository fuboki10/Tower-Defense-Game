import pygame
import os
from .tower import Tower

imgs = []
for i in range(3):
    tmp = []
    for j in range(3):
        img = pygame.image.load(os.path.join("assets/towers/1/level_" + str(i+1), str(j+1) + ".png"))
        tmp.append(pygame.transform.scale(img, (img.get_width() // 2, img.get_height() // 2)))
    imgs.append(tmp)

class StoneTower(Tower):
    def __init__(self, x: int, y: int):
        super().__init__(x, y)
        self.imgs = imgs
        self.width = imgs[0][0].get_width()
        self.height = imgs[0][0].get_height()
        self.pos = []
        self.pos.append((self.x - self.width // 2, self.y - self.height // 2))
        self.pos.append((self.x - self.width // 2, self.y - self.height // 6))
        self.pos.append((self.x - self.width // 2, self.y))
        self.move_range = []
        self.move_range.append((self.y - self.height // 2, self.y - self.height // 2))
        self.move_range.append((self.y - self.height // 6, self.y - self.height // 6 - self.height // 3))
        self.move_range.append((self.y, self.y - self.height // 3))
        self.mode = {'up': 0, 'down': 1, 'stop': 2}
        self.current_mode = self.mode['stop']
        self.selected = False
        self.speed = 10  # 100 moves per second

    def draw(self, window):
        """
        Draws StoneTower
        :param window: Surface
        :return: None
        """
        self.draw_radius(window)
        super().draw_health_bar(window)
        img = self.imgs[self.level - 1]
        window.blit(img[1], self.pos[1])
        window.blit(img[0], self.pos[0])
        window.blit(img[2], self.pos[2])

    def animate(self, dt):
        """
        Animates the tower
        :return: None
        """
        self.timer += dt
        if self.current_mode == self.mode['up']:
            pos1 = list(self.pos[1])
            pos2 = list(self.pos[2])
            pos1[1] -= self.timer // self.speed
            pos2[1] -= self.timer // self.speed
            self.pos[1] = tuple(pos1)
            self.pos[2] = tuple(pos2)
            if pos1[1] <= self.move_range[1][1] or pos2[1] <= self.move_range[2][1]:
                self.current_mode = self.mode['down']
                pos1[1] = self.move_range[1][1]
                pos2[1] = self.move_range[2][1]
                self.pos[1] = tuple(pos1)
                self.pos[2] = tuple(pos2)

        elif self.current_mode == self.mode['down']:
            pos1 = list(self.pos[1])
            pos2 = list(self.pos[2])
            pos1[1] += self.timer // self.speed
            pos2[1] += self.timer // self.speed
            self.pos[1] = tuple(pos1)
            self.pos[2] = tuple(pos2)
            if pos1[1] >= self.move_range[1][0] or pos2[1] >= self.move_range[2][0]:
                self.current_mode = self.mode['stop']
                pos1[1] = self.move_range[1][0]
                pos2[1] = self.move_range[2][0]
                self.pos[1] = tuple(pos1)
                self.pos[2] = tuple(pos2)

        self.timer = self.timer % self.speed

    def attack(self):
        """
        Attack
        :return: None
        """
        if self.current_mode == self.mode['stop']:
            self.current_mode = self.mode['up']

    def update(self, dt):
        self.animate(dt)

        if self.selected:
            self.attack()
