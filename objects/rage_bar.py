from init.gameinitializers import *
from objects.cat import *

class Rage_Bar(pygame.sprite.Sprite):
    def __init__(self):
        self.BAR_WIDTH = 200
        self.BAR_HEIGHT = 30
        self.x = (WIDTH - self.BAR_WIDTH) // 2
        self.y = 10
        self.fill = (1 // 100) * self.BAR_WIDTH
        self.outline_rect = pygame.Rect(self.x, self.y, self.BAR_WIDTH, self.BAR_HEIGHT)
        self.fill_rect = pygame.Rect(self.x+3, self.y, self.fill, self.BAR_HEIGHT)

    def draw_shield_bar(self, screen, cat_class):
        if cat_class.anger < 0:
            cat_class.anger = 0
        
        self.fill = (cat_class.anger / 100) * (self.BAR_WIDTH-2)
        self.fill_rect = pygame.Rect(self.x+2, self.y, self.fill, self.BAR_HEIGHT)

        if cat_class.anger > 75:
            pygame.draw.rect(screen, RED, self.fill_rect)
            pygame.draw.rect(screen, WHITE, self.outline_rect, 2)

        elif cat_class.anger > 50:
            pygame.draw.rect(screen, POWER, self.fill_rect)
            pygame.draw.rect(screen, WHITE, self.outline_rect, 2)
            
        elif cat_class.anger > 25:
            pygame.draw.rect(screen, BANANA, self.fill_rect)
            pygame.draw.rect(screen, WHITE, self.outline_rect, 2)

        else:
            pygame.draw.rect(screen, GREEN, self.fill_rect)
            pygame.draw.rect(screen, WHITE, self.outline_rect, 2)
