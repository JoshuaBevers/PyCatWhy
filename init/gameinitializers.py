from pygame.locals import (
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_ESCAPE,
    KEYDOWN,
    QUIT,
    K_m
)
import pygame

# define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
CLEAR = (0, 0, 0, 0)
POWER = (200, 100, 10)

# define game screen sizing and fps
WIDTH = 780
HEIGHT = 780
FPS = 40

# Import pygame.locals to establish necessary key commands

# define the cat start point and speed

CAT_START = (WIDTH // 2, HEIGHT // 2)
CAT_SPEED = 5

MENU_LIST = ['images/title-scren.png', 'images/level-2.png', 'images/level-3.png', 'images/level-4.png', 'images/level-5.png', 'images/level-6.png', 'images/level-7.png', 'images/level-8.png', 'images/level-9.png', 'images/level-10.png', 'images/you-win.png', 'images/you-lose.png']

