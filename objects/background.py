import pygame
from init.gameinitializers import *


class Background(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.background = pygame.image.load('images/bg-field-large2.png')
        self.rect = self.background.get_rect()
        self.rect.left, self.rect.top = (0, 0)
        self.music = pygame.mixer.music


    def start_music(self):
        self.music.set_volume = (0.5)
        self.music.load('sounds/Mus-zz-megalovania.ogg')
        self.music.play(-1)

    def stop_music(self):
        self.music.stop()
