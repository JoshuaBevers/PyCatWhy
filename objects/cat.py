import pygame
from init.gameinitalizers import *

class Cat(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((40, 34))
        self.image.fill(BLUE)
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH // 2, HEIGHT // 2)
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