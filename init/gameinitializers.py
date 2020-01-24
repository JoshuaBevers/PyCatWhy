from pygame.locals import (
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_ESCAPE,
    KEYDOWN,
    QUIT,
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
BANNANA = (227, 207, 87)

# define game screen sizing and fps
WIDTH = 780
HEIGHT = 780
FPS = 40

# Import pygame.locals to establish necessary key commands

# define the cat start point and speed

CAT_START = (WIDTH // 2, HEIGHT // 2)
CAT_SPEED = 5
