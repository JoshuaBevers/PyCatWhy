import pygame
from init.gameinitializers import *


class Text(pygame.sprite.Sprite):
    def __init__(self, text, size, horizontal_loc, vertical_loc):
        super().__init__()
        pygame.sprite.Sprite.__init__(self)
        self.width = len(text)*size
        self.height = size
        self.font = pygame.font.Font('slkscrb.ttf', size)
        self.font.set_bold(True)

        self.image = self.font.render(text, True, BLACK)
        self.rect = self.image.get_rect()
        self.rect.center = (horizontal_loc, vertical_loc)

        self.duration = 0


    def display_check(self, screen):
        if self.duration > 0:
            screen.blit(self.image, self.rect)
            self.duration -= 1

        elif self.duration <= 0:
            self.display_off()

    def display_on(self, num):
        self.duration = num

    def display_off(self):
        self.duration = 0

    def menu_show(self, screen):
        screen.blit(self.image, self.rect)
