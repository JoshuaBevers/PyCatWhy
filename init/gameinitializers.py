# Import pygame.locals to establish necessary key commands
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


class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
CLEAR = (0, 0, 0, 0)
POWER = (200, 100, 10)
BANANA = (227, 207, 87)

# define game screen sizing and fps
WIDTH = 780
HEIGHT = 780
FPS = 40

# define optional font locations
FONT_WIDTH_CENTER = (WIDTH / 2)
FONT_WIDTH_LEFT = (WIDTH / 4) * 1
FONT_WIDTH_RIGHT = (WIDTH / 4) * 3

FONT_HEIGHT_CENTER = (HEIGHT / 2)
FONT_HEIGHT_TOP_T = (HEIGHT / 7)
FONT_HEIGHT_TOP_C = (HEIGHT / 7) * 2
FONT_HEIGHT_TOP_B = (HEIGHT / 7) * 3
FONT_HEIGHT_BOTTOM_T = (HEIGHT / 7) * 4
FONT_HEIGHT_BOTTOM_C = (HEIGHT / 7) * 5
FONT_HEIGHT_BOTTOM_B = (HEIGHT / 7) * 6

# define the cat start point and speed
CAT_START = (WIDTH // 2, HEIGHT // 2)
CAT_SPEED = 5

MENU_LIST = ['images/title-scren.png', 'images/level-2.png', 'images/level-3.png', 'images/level-4.png', 'images/level-5.png', 'images/level-6.png', 'images/level-7.png', 'images/level-8.png', 'images/level-9.png', 'images/level-10.png', 'images/you-win.png', 'images/you-lose.png']

end_game_sit = 0
