import pygame

# define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
CLEAR = (0, 0, 0, 0)

# define game screen sizing and fps
WIDTH = 780
HEIGHT = 780
FPS = 30

# Import pygame.locals to establish necessary key commands
from pygame.locals import (
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_ESCAPE,
    KEYDOWN,
    QUIT,
)

# define the cat start point

CAT_START = (WIDTH // 2, HEIGHT // 2)
CAT_SPEED = 3