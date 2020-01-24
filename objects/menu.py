import pygame
from init.gameinitializers import *

class Menu(pygame.sprite.Sprite):
    def __init__(self, menu_image):
        pygame.sprite.Sprite.__init__(self)
        self.menu_image = menu_image
        self.background = pygame.image.load(self.menu_image)
        self.rect = self.background.get_rect()
        self.rect.left, self.rect.top = (0, 0)
        