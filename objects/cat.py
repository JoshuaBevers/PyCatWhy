import pygame
from init.gameinitializers import *


class Cat(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.width = 80
        self.height = 68
        self.image = pygame.Surface(
            [self.width, self.height], pygame.SRCALPHA, 32)
        self.image.convert_alpha()
        self.sitting = pygame.image.load(
            'images/catspritesx4-transparent-sitting.png')
        self.staring = pygame.image.load(
            'images/catspritesx4-transparent-staring.png')
        self.running_left = [pygame.image.load(
            'images/catspritesx4-transparent-running1.png'), pygame.image.load('images/catspritesx4-transparent-running2.png')]
        self.running_right = [pygame.transform.flip(
            self.running_left[0], True, False), pygame.transform.flip(self.running_left[1], True, False)]

        self.running_sprite = self.running_left[0]
        self.rect = self.image.get_rect()
        self.rect.center = CAT_START
        self.direction_x = "LEFT"
        self.direction_y = "UP"

        self.meow = pygame.mixer.Sound('sounds/cat-meow.wav')
        self.screech = pygame.mixer.Sound('sounds/cat-screech.wav')
        self.growl = pygame.mixer.Sound('sounds/cat-growl.wav')

        # Variables.
        self.anger = 0
        self.level = 0
        self.end_game_sit = 0


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
        if self.direction_y == "STOP" and self.direction_x == "STOP":
            self.rect.x += 0
            self.rect.y += 0
        self.movement()

    def change_direction(self, point, sound=False):
        if point == "top_left":
            self.direction_x = "RIGHT"
            self.direction_y = "DOWN"
            if sound:
                self.meow.play()
        elif point == "top_right":
            self.direction_x = "LEFT"
            self.direction_y = "DOWN"
            if sound:
                self.meow.play()
        elif point == "bottom_left":
            self.direction_x = "RIGHT"
            self.direction_y = "UP"
            if sound:
                self.meow.play()
        elif point == "bottom_right":
            self.direction_x = "LEFT"
            self.direction_y = "UP"
            if sound:
                self.meow.play()

    def movement(self):
        if self.rect.x % 30 == 0:
            if self.running_sprite == self.running_left[0] or self.running_sprite == self.running_right[0]:
                if self.direction_x == "LEFT":
                    self.running_sprite = self.running_left[1]
                elif self.direction_x == "RIGHT":
                    self.running_sprite = self.running_right[1]
            elif self.running_sprite == self.running_left[1] or self.running_sprite == self.running_right[1]:
                if self.direction_x == "LEFT":
                    self.running_sprite = self.running_left[0]
                elif self.direction_x == "RIGHT":
                    self.running_sprite = self.running_right[0]
        elif self.direction_x == "STOP" and self.direction_y == "STOP":
            if self.end_game_sit <= 25:
                self.running_sprite = self.sitting
            else:
                self.running_sprite = self.staring
