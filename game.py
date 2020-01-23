# Necessary imports
from pygame.locals import *
import pygame
import sys
import time
import random
from init.gameinitalizers import *
from objects.cat import Cat
from objects.orange import Orange
from os import path
from sounds import *
from pygame import mixer

# Space allocated for creating and adding variables.
cat = Cat()
orange = Orange(GREEN, 20, 15)
clock = pygame.time.Clock()
all_sprites = pygame.sprite.Group()
all_sprites.add(cat)
orangeOBT = pygame.sprite.Group()

# pygame.mixer.pre_init(44100, 16, 2, 4096)
# Initialize pygame and create window
pygame.init()
pygame.mixer.init(44100, -16, 2, 2048)
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("PyCatWhy?!")
SPAWN_SPEED = 1000

# sounds


# If the loops is -1 then the music will repeat indefinitely.

# timer var


spawn_orange = pygame.USEREVENT + 1

pygame.time.set_timer(spawn_orange + 1, SPAWN_SPEED)


def create_orange():
    all_sprites.add(orange)


### Game loop ###
running = True
while running:
    # variables being kept track of at the start of the game.
    start_ticks = pygame.time.get_ticks()
    # Keep loop running at the right speed
    clock.tick(FPS)
    # Process input (events)
    for event in pygame.event.get():
        if event.type == spawn_orange + 1:
            for i in range(1):
                o = Orange(BLUE, 20, 15)
                all_sprites.add(o)
                orangeOBT.add(o)

                # calling the function wheever we get timer event.

        # check for closing window
        if event.type == KEYDOWN and event.key == K_ESCAPE:
            running = False
        elif event.type == pygame.QUIT:
            running = False

    # Update
    all_sprites.update()
    orangeOBT.update()

    # Draw / render
    screen.fill(BLACK)
    all_sprites.draw(screen)
    orangeOBT.draw(screen)

    # *after* drawing everything, flip the display
    pygame.display.flip()

    # possibly spawns in an orange.

    # Get mouse button state and mouse position if pressed
    if pygame.mouse.get_pressed()[0]:
        mouse_coords = pygame.mouse.get_pos()
        mouse_position = [int(mouse_coords[0]), int(mouse_coords[1])]

        print(mouse_position)


# Pygame end
pygame.quit()
