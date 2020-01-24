import pygame
from init.gameinitializers import *


class Menu(pygame.sprite.Sprite):
    def __init__(self, menu_image):
        pygame.sprite.Sprite.__init__(self)
        self.menu_image = menu_image
        self.background = pygame.image.load(self.menu_image)
        self.rect = self.background.get_rect()
        self.rect.left, self.rect.top = (0, 0)
        
    def draw_text(surf, text, size, x, y):
        font_name = pygame.font.match_font('arial')

        font = pygame.font.Font(font_name, size)
        text_surface = font.render(text, True, WHITE)
        text_rect = text_surface.get_rect()
        text_rect.midtop = (x, y)
        surf.blit(text_surface, text_rect)

    def show_menu_screen(self, screen, clock):
        screen.blit(self.background, self.rect)
        # draw_text(screen, "Get the Cat to the Carrier", 64, WIDTH / 2, HEIGHT / 4)
        pygame.display.flip()
        waiting = True
        while waiting:
            clock.tick(FPS)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                # Any key press will start the game
                if event.type == pygame.MOUSEBUTTONDOWN:
                    waiting = False