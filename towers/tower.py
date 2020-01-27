import pygame


class Tower:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y
        self.width = 0
        self.height = 0
        self.sell_price = [0, 0, 0]
        self.buy_price = [0, 0, 0]
        self.level = 1
        self.imgs = []
        self.damage = 1
        self.selected = False
        self.menu = None
        self.range = 100
        self.max_health = 10
        self.health = self.max_health
        self.place_color = (0, 0, 255, 100)
        self.timer = 0

    def draw(self, window):
        """
        Draws the Tower
        :param window: surface
        :return: None
        """
        img = self.imgs[self.level - 1]
        window.blit(img, (self.x - img.get_width() / 2, self.y - img.get_height() / 2))

    def move(self, x: int, y: int):
        """
        Change Tower Position
        :param x: int
        :param y: int
        :return: None
        """
        self.x = x
        self.y = y

    def click(self, x: int, y: int):
        """
        Returns if tower has been clicked on and select it
        :param x: int
        :param y: int
        :return: Bool
        """
        if self.x + self.width // 2 >= x >= self.x - self.width // 2:
            if self.y + self.height // 2 >= y >= self.y - self.height // 2:
                self.selected = True
                return True
        self.selected = False
        return False

    def sell(self):
        """
        Returns sell price
        :return: int
        """
        return self.sell_price[self.level - 1]

    def upgrade(self):
        """
        updrages the tower
        :return: None
        """
        if self.level < len(self.imgs):
            self.level += 1
            self.damage += 1

    def move(self, x: int, y: int):
        """
        move the tower
        :param x: int
        :param y: int
        :return: None
        """
        self.x = x
        self.y = y

    def draw_health_bar(self, window):
        """
        Draw Health bar
        :param window: surface
        :return: None
        """
        length = 40
        move_by = round(length / self.max_health)
        health_bar = move_by * self.health

        pygame.draw.rect(window, (255, 0, 0), (self.x - self.width // 2 + length // 2, self.y - self.height * 3 // 4, length, 5), 0)
        pygame.draw.rect(window, (0, 255, 0), (self.x - self.width // 2 + length // 2, self.y - self.height * 3 // 4, health_bar, 5), 0)

    def draw_radius(self, window):
        """
        draw range circle
        :param window: surface
        :return: None
        """
        if self.selected:
            surface = pygame.Surface((self.range * 4, self.range * 4), pygame.SRCALPHA, 32)
            pygame.draw.circle(surface, (128, 128, 128, 100), (self.range, self.range), self.range, 0)

            window.blit(surface, (self.x - self.range, self.y - self.range))

    def draw_placement(self, window):
        """
        draw place circle
        :param window: surface
        :return: None
        """
        surface = pygame.Surface((self.range * 4, self.range * 4), pygame.SRCALPHA, 32)
        pygame.draw.circle(surface, self.place_color, (50, 50), 50, 0)

        window.blit(surface, (self.x - 50, self.y - 50))

    def update(self, dt):
        pass
