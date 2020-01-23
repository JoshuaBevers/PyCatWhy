# Necessary imports
from pygame.locals import *
from objects.orange import *
import pygame
import sys
import time
import random
from init.gameinitializers import *
from objects.cat import *
from objects.click_box import *

# pygame.mixer.pre_init(44100, 16, 2, 4096)
# Initialize pygame and create window
pygame.init()
pygame.mixer.init(44100, -16, 2, 2048)
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("PyCatWhy?!")
SPAWN_SPEED = 1000

# sounds


# timer var

spawn_orange = pygame.USEREVENT + 1

pygame.time.set_timer(spawn_orange + 1, SPAWN_SPEED)


# Space allocated for creating and adding variables.
cat = Cat()
orange = Orange(GREEN, 40, 40)

top_left = Click_Box('top_left')
top_right = Click_Box('top_right')
bottom_left = Click_Box('bottom_left')
bottom_right = Click_Box('bottom_right')
clock = pygame.time.Clock()
all_sprites = pygame.sprite.Group()
click_boxes = pygame.sprite.Group()
obsticals = pygame.sprite.Group()
all_sprites.add(cat)
click_boxes.add(top_left, top_right, bottom_left, bottom_right)


def cattitude(surf, x, y, pct):
    if pct < 0:
        pct = 0
    BAR_LENGTH = 160
    BAR_HEIGHT = 30
    fill = (pct / 100) * BAR_LENGTH
    outline_rect = pygame.Rect(x, y, BAR_LENGTH, BAR_HEIGHT)
    fill_rect = pygame.Rect(x, y, fill, BAR_HEIGHT)
    pygame.draw.rect(surf, RED, fill_rect)
    pygame.draw.rect(surf, BLACK, outline_rect, 2)


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
                obsticals.add(o)

                # calling the function wheever we get timer event.

        # check for closing window
        if event.type == KEYDOWN and event.key == K_ESCAPE:
            running = False
        elif event.type == pygame.QUIT:
            running = False

        # clicking on cat
        if event.type == pygame.MOUSEBUTTONDOWN:
            attitude = random.randint(1, 30)
            x, y = event.pos
            if top_left.rect.collidepoint(x, y):
                cat.change_direction('top_left')
                if attitude == 1:
                    print("This cat has attitude!")
                    changeDir = random.randint(1, 3)
                    if changeDir == 1:
                        cat.change_direction('bottom_left')
                    if changeDir == 2:
                        cat.change_direction('top_right')
                    if changeDir == 3:
                        cat.change_direction('bottom_right')
            if top_right.rect.collidepoint(x, y):
                cat.change_direction('top_right')
                if attitude == 1:
                    print("This cat has attitude!")
                    changeDir = random.randint(1, 3)
                    if changeDir == 1:
                        cat.change_direction('bottom_left')
                    if changeDir == 2:
                        cat.change_direction('top_left')
                    if changeDir == 3:
                        cat.change_direction('bottom_right')
            if bottom_left.rect.collidepoint(x, y):
                cat.change_direction('bottom_left')
                if attitude == 1:
                    print("This cat has attitude!")
                    changeDir = random.randint(1, 3)
                    if changeDir == 1:
                        cat.change_direction('bottom_left')
                    if changeDir == 2:
                        cat.change_direction('top_right')
                    if changeDir == 3:
                        cat.change_direction('bottom_right')
            if bottom_right.rect.collidepoint(x, y):
                cat.change_direction('bottom_right')
                if attitude == 1:
                    print("This cat has attitude!")
                    changeDir = random.randint(1, 3)
                    if changeDir == 1:
                        cat.change_direction('bottom_left')
                    if changeDir == 2:
                        cat.change_direction('top_right')
                    if changeDir == 3:
                        cat.change_direction('top_left')

    # Update
    all_sprites.update()
    click_boxes.update(cat)

    # Draw / render
    screen.fill(BLUE)
    all_sprites.draw(screen)
    click_boxes.draw(screen)
    cattitude(screen, 350, 10, cat.anger)

    if cat.running_sprite == cat.running[0] and cat.rect.x % 50 == 0:
        cat.running_sprite = cat.running[1]
    elif cat.running_sprite == cat.running[1] and cat.rect.x % 50 == 0:
        cat.running_sprite = cat.running[0]
    screen.blit(cat.running_sprite, cat.rect)

    # *after* drawing everything, flip the display
    pygame.display.flip()


# Pygame end
pygame.quit()
