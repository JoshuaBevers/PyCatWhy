import pygame
from init.gameinitializers import *

class Cat(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((40, 34))
        self.image.fill(BLUE)
        self.sitting = pygame.image.load('images/catspritesx2-transparent-sitting.png')
        self.running = [pygame.image.load('images/catspritesx2-transparent-running1.png'), pygame.image.load('images/catspritesx2-transparent-running2.png')]
        self.running_sprite = self.running[0]
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

    def change_direction(self):
        if self.direction_x == "LEFT":
            self.direction_x = "RIGHT"
        if self.direction_x == "RIGHT":
            self.direction_x = "LEFT"
        if self.direction_y == "DOWN":
            self.direction_y = "UP"
        if self.direction_y == "UP":
            self.direction_y = "DOWN"

