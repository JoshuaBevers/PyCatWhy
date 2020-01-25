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
        if cat_x < WIDTH // 2 and cat_y < HEIGHT // 2:
            self.rect.x = random.randrange(WIDTH//2, WIDTH-self.width)
            self.rect.y = random.randrange(HEIGHT//2, HEIGHT-self.height)
        elif cat_x > WIDTH // 2 and cat_y < HEIGHT // 2:
            self.rect.x = random.randrange(WIDTH//2)
            self.rect.y = random.randrange(HEIGHT//2, HEIGHT-self.height)
        elif cat_x > WIDTH // 2 and cat_y > HEIGHT // 2:
            self.rect.x = random.randrange(WIDTH//2)
            self.rect.y = random.randrange(self.height, HEIGHT//2)
        elif cat_x < WIDTH // 2 and cat_y > HEIGHT // 2:
            self.rect.x = random.randrange(WIDTH//2, WIDTH-self.width)
            self.rect.y = random.randrange(self.height, HEIGHT//2)
        else:
            self.rect.x = random.randrange(WIDTH-self.width)
            self.rect.y = random.randrange(self.height, HEIGHT-self.height)
