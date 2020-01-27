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

def random_spawn():
    num = random.randint(1, 2)
    if num == 1:
        return ["LEFT", "UP"]
    if num == 2:
        return ["RIGHT", "DOWN"]


class Orange(pygame.sprite.Sprite):
    def __init__(self, color, width, height, cat):
        # Call the parent class (Sprite) constructor
        super().__init__()
        pygame.sprite.Sprite.__init__(self)
        # self.image = pygame.Surface([width, height], pygame.SRCALPHA, 32)
        # self.image.convert_alpha()
        self.image = pygame.image.load('images/orange.png')
        self.rect = self.image.get_rect()
        self.rect.x = set_start_x(cat)
        self.rect.y = set_start_y(cat)

        self.direction_x = random_spawn()[0]
        self.direction_y = random_spawn()[1]

    def update(self):
        if self.direction_x == "LEFT":
            self.rect.x += 5
            if self.rect.right >= WIDTH:
                self.direction_x = "RIGHT"
        if self.direction_x == "RIGHT":
            self.rect.x -= 5
            if self.rect.left <= 0:
                self.direction_x = "LEFT"
        if self.direction_y == "DOWN":
            self.rect.y += 5
            if self.rect.bottom >= HEIGHT:
                self.direction_y = "UP"
        if self.direction_y == "UP":
            self.rect.y -= 5
            if self.rect.top <= 0:
                self.direction_y = "DOWN"

    def die(self):
        pygame.sprite.Sprite.kill(self)
