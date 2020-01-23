import pygame
from init.gameinitializers import *


class Cat(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((40, 34))
        self.sitting = pygame.image.load(
            'images/catspritesx2-transparent-sitting.png')
        self.running = [pygame.image.load('images/catspritesx2-transparent-running1.png'),
                        pygame.image.load('images/catspritesx2-transparent-running2.png')]
        self.running_sprite = self.running[0]
        self.rect = self.image.get_rect()
        self.rect.center = CAT_START
        self.direction_x = "LEFT"
        self.direction_y = "UP"
        self.anger = 0

    def update(self):
        # interact with screen edges
        if self.direction_x == "RIGHT":
            self.rect.x += CAT_SPEED
            if self.rect.right >= WIDTH:
                self.direction_x = "LEFT"
        if self.direction_x == "LEFT":
            self.rect.x -= CAT_SPEED
            if self.rect.left <= 0:
                self.direction_x = "RIGHT"
        if self.direction_y == "DOWN":
            self.rect.y += CAT_SPEED
            if self.rect.bottom >= HEIGHT:
                self.direction_y = "UP"
        if self.direction_y == "UP":
            self.rect.y -= CAT_SPEED
            if self.rect.top <= 0:
                self.direction_y = "DOWN"

    def change_direction(self, point):
        if point == "top_left":
            self.direction_x = "RIGHT"
            self.direction_y = "DOWN"
        elif point == "top_right":
            self.direction_x = "LEFT"
            self.direction_y = "DOWN"
        elif point == "bottom_left":
            self.direction_x = "RIGHT"
            self.direction_y = "UP"
        elif point == "bottom_right":
            self.direction_x = "LEFT"
            self.direction_y = "UP"
