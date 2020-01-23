import pygame
from init.gameinitializers import *

class Background(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.background = pygame.image.load('images/bg-field-large.png')
        self.rect = self.background.get_rect()
        self.rect.left, self.rect.top = (0, 0)
        self.music = pygame.mixer.music

    def start_music(self):
        self.music.load('sounds/Undertale-Megalovania.mp3')
        self.music.play(-1)

