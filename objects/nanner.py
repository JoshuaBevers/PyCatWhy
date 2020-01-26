import pygame
import random
from init.gameinitializers import *

def set_start_x(cat):
    while True:
        x = random.randint(0, WIDTH)
        if x < cat.rect.left - cat.width or x > cat.rect.right + cat.width:
            return x
            break

def set_start_y(cat):
    while True:
        y = random.randint(0, HEIGHT)
        if y < cat.rect.top - cat.height or y > cat.rect.bottom + cat.height:
            return y
            break


class Nanner(pygame.sprite.Sprite):
    def __init__(self, color, width, height, cat):
        # Call the parent class (Sprite) constructor
        super().__init__()
        pygame.sprite.Sprite.__init__(self)
        # self.image = pygame.Surface([width, height], pygame.SRCALPHA, 32)
        # self.image.convert_alpha()
        self.image = pygame.image.load('images/banana.png')
        self.rect = self.image.get_rect()
        self.rect.x = set_start_x(cat)
        self.rect.y = set_start_y(cat)
        self.direction_x = "LEFT"
        self.direction_y = "UP"
