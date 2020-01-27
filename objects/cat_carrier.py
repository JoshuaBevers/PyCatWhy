import pygame
import random
from init.gameinitializers import *


class Carrier(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.width = 100
        self.height = 86
        self.image = pygame.Surface(
            [self.width, self.height], pygame.SRCALPHA, 32)
        self.image.convert_alpha()
        self.sprite = pygame.image.load('images/cat-carrier4.png')
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(WIDTH-self.width)
        self.rect.y = random.randrange(self.height, HEIGHT-self.height)

    def respawn(self, cat_x, cat_y):
        while True:
            x = random.randint(0, WIDTH-self.width)
            if cat_x < x - WIDTH//6 or cat_x > x + WIDTH//6:
                self.rect.x = x
                break
        while True:
            y = random.randint(self.height, HEIGHT-self.height)
            if cat_y < y - HEIGHT//6 or cat_y > y + HEIGHT//6:
                self.rect.y = y
                break
