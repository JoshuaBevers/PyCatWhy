from init.gameinitializers import *

class Rage_Bar(pygame.sprite.Sprite):
    def __init__(self):
        self.BAR_LENGTH = 100
        self.BAR_HEIGHT = 10
        self.rage = 0 
        self.outline_rect = pygame.Rect(x, y, self.BAR_LENGTH, self.BAR_HEIGHT)
        self.fill_rect = pygame.Rect(x, y, self.fill, self.BAR_HEIGHT)

    def draw_shield_bar(surf, x, y, pct):
        if pct < 0:
            pct = 0
        BAR_LENGTH = 100
        BAR_HEIGHT = 10
        fill = (pct / 100) * BAR_LENGTH
        outline_rect = pygame.Rect(x, y, BAR_LENGTH, BAR_HEIGHT)
        fill_rect = pygame.Rect(x, y, fill, BAR_HEIGHT)
        pygame.draw.rect(surf, GREEN, fill_rect)
        pygame.draw.rect(surf, WHITE, outline_rect, 2)
        if fill < 30:
            pygame.draw.rect(surf, RED, fill_rect)