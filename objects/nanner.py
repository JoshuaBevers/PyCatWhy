import pygame
import random
from init.gameinitializers import *


class Nanner(pygame.sprite.Sprite):
    def __init__(self, color, width, height):
        # Call the parent class (Sprite) constructor
        super().__init__()
        pygame.sprite.Sprite.__init__(self)
        # self.image = pygame.Surface([width, height], pygame.SRCALPHA, 32)
        # self.image.convert_alpha()
        self.image = pygame.image.load('images/banana.png')
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(WIDTH)
        self.rect.y = random.randrange(HEIGHT)
        self.direction_x = "LEFT"
        self.direction_y = "UP"
