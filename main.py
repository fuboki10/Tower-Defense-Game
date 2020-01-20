import pygame
from main_menu.main_menu import MainMenu

if __name__ == "__main__":
    pygame.init()
    window = pygame.display.set_mode((1000, 700))
    mainMenu = MainMenu(window, 1000, 700)
    mainMenu.run()
