import pygame
from init.gameinitializers import *


class Menu(pygame.sprite.Sprite):
    def __init__(self, menu_image):
        pygame.sprite.Sprite.__init__(self)
        self.background = pygame.image.load(menu_image)
        self.rect = self.background.get_rect()
        self.rect.topleft = (0, 0)
        
    def show_menu_screen(self, screen, clock):
        screen.blit(self.background, self.rect)
        pygame.display.flip()
        waiting = True
        while waiting:
            clock.tick(FPS)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                # click the mouse to start
                if event.type == pygame.MOUSEBUTTONDOWN:
                    waiting = False


    def draw_text(surf, text, size, x, y):
        font_name = pygame.font.match_font('arial')

        font = pygame.font.Font(font_name, size)
        text_surface = font.render(text, True, WHITE)
        text_rect = text_surface.get_rect()
        text_rect.midtop = (x, y)
        surf.blit(text_surface, text_rect)