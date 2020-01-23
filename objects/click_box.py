import pygame
from init.gameinitializers import *

class Click_Box(pygame.sprite.Sprite):
    def __init__(self, location):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((20, 17), pygame.SRCALPHA, 32)
        self.image.convert_alpha()
        self.rect = self.image.get_rect()
        self.location = location
        if self.location == 'top_left':
            self.rect.bottomright = CAT_START
        elif self.location == 'top_right':
            self.rect.bottomleft = CAT_START
        elif self.location == 'bottom_left':
            self.rect.topright = CAT_START
        else:
            self.rect.topleft = CAT_START

    def update(self, cat):
        if self.location == 'top_left':
            self.rect.bottomright = cat.rect.center
        elif self.location == 'top_right':
            self.rect.bottomleft = cat.rect.center
        elif self.location == 'bottom_left':
            self.rect.topright = cat.rect.center
        else:
            self.rect.topleft = cat.rect.center

    