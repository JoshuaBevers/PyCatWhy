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
        # pygame.draw.ellipse(self.image, WHITE, [0, 0, 100, 86])
        self.image.convert_alpha()
        self.sprite = pygame.image.load(
            'images/cat-carrier2.png')
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(WIDTH-self.width)
        self.rect.y = random.randrange(self.height, HEIGHT-self.height)


# Might need to add this later.
    # def update(self):
    #     if self.direction_x == "LEFT":
    #         self.rect.x += 5
    #         if self.rect.right >= WIDTH:
    #             self.direction_x = "RIGHT"
    #     if self.direction_x == "RIGHT":
    #         self.rect.x -= 5
    #         if self.rect.left <= 0:
    #             self.direction_x = "LEFT"
    #     if self.direction_y == "DOWN":
    #         self.rect.y += 5
    #         if self.rect.bottom >= HEIGHT:
    #             self.direction_y = "UP"
    #     if self.direction_y == "UP":
    #         self.rect.y -= 5
    #         if self.rect.top <= 0:
    #             self.direction_y = "DOWN"
