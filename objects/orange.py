import pygame
import random
from init.gameinitializers import *


class Orange(pygame.sprite.Sprite):
    def __init__(self, color, width, height):
        # Call the parent class (Sprite) constructor
        super().__init__()
        pygame.sprite.Sprite.__init__(self)
        # self.image = pygame.Surface([width, height], pygame.SRCALPHA, 32)
        # self.image.convert_alpha()
        self.image = pygame.image.load('images/orange.png')
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(WIDTH)
        self.rect.y = random.randrange(HEIGHT)

        self.direction_x = "LEFT"
        self.direction_y = "UP"

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
    
    