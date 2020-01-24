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

        


    # def draw_text(surf, text, size, x, y):
    #     font_name = pygame.font.match_font('arial')

    #     font = pygame.font.Font(font_name, size)
    #     text_surface = font.render(text, True, WHITE)
    #     text_rect = text_surface.get_rect()
    #     text_rect.midtop = (x, y)
    #     surf.blit(text_surface, text_rect)

    def change_level_screen(self, new_cat_level):
        self.background = pygame.image.load(self.menu_list[new_cat_level])

    