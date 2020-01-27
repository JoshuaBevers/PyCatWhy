import pygame
from init.gameinitializers import *


class Menu(pygame.sprite.Sprite):
    def __init__(self, cat_level):
        pygame.sprite.Sprite.__init__(self)
        self.menu_list = MENU_LIST
        self.background = pygame.image.load(self.menu_list[cat_level])
        self.rect = self.background.get_rect()
        self.rect.topleft = (0, 0)
        

    def show_menu_screen(self, screen, clock):
        screen.blit(self.background, self.rect)
        pygame.display.flip()
        waiting = True
        while waiting:
            clock.tick(FPS)
            for event in pygame.event.get():
                if event.type == KEYDOWN and event.key == K_ESCAPE or event.type == pygame.QUIT:
                    pygame.quit()
                    exit(0)
                # click the mouse to start
                if event.type == pygame.MOUSEBUTTONDOWN:
                    waiting = False

    def change_level_screen(self, new_cat_level):
        self.background = pygame.image.load(self.menu_list[new_cat_level])

    