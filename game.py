# Necessary imports
from pygame.locals import *
from objects.orange import *
import pygame
import sys
import time
import random
from init.gameinitializers import *
from objects.click_box import *
from objects.background import *
from objects.cat_carrier import *
from objects.cat import *
from objects.menu import *
from objects.text import *

pygame.init()
pygame.mixer.init(44100, -16, 2, 2048)
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("PyCatWhy?!?")
SPAWN_SPEED = 1000

# sounds


# timer var

spawn_orange = pygame.USEREVENT + 1

pygame.time.set_timer(spawn_orange + 1, SPAWN_SPEED)


# Space allocated for creating and adding variables.
bg = Background()
cat = Cat()
goal = Carrier()
orange = Orange(POWER, 40, 40)
menu = Menu('images/title-scren.png')

top_left = Click_Box('top_left')
top_right = Click_Box('top_right')
bottom_left = Click_Box('bottom_left')
bottom_right = Click_Box('bottom_right')

text_ouch = Text("Meowch!", 30, FONT_WIDTH_RIGHT, FONT_HEIGHT_TOP_T)
text_attitude = Text("This cat has attitude!", 30, FONT_WIDTH_CENTER, FONT_HEIGHT_CENTER)
text_end_top = Text("The cat has fucked off!", 50, FONT_WIDTH_CENTER, FONT_HEIGHT_TOP_T)
text_end_bottom = Text("You lose.", 20, FONT_WIDTH_CENTER, FONT_HEIGHT_TOP_T)

clock = pygame.time.Clock()

# All sprites group set
all_sprites = pygame.sprite.Group()
all_sprites.add(cat)
all_sprites.add(goal)

# Obstacle group set
obstacle = pygame.sprite.Group()
obstacle.add(orange)

# Player group set
player = pygame.sprite.Group()
player.add(cat)

# Clickboxes group set
click_boxes = pygame.sprite.Group()
click_boxes.add(top_left, top_right, bottom_left, bottom_right)

# Cat carrier group set
carrier = pygame.sprite.Group()
carrier.add(goal)

# Text group set
text = pygame.sprite.Group()
carrier.add(text_ouch, text_attitude, text_end_top, text_end_bottom)

# Start music!
bg.start_music()


# Create functions
def angerRises():
    cat.anger += 10
    cat.screech.play(fade_ms=1).fadeout(1000)
    print(cat.anger)


def angerCheck():
    if cat.anger == 100:
        print("This rage cannot be contained!")


def cattitude(surf, x, y, pct):
    if pct < 0:
        pct = 0
    BAR_LENGTH = 160
    BAR_HEIGHT = 30
    fill = (pct / 100) * BAR_LENGTH
    outline_rect = pygame.Rect(x, y, BAR_LENGTH, BAR_HEIGHT)
    fill_rect = pygame.Rect(x + 3, y, fill, BAR_HEIGHT)
    pygame.draw.rect(surf, RED, fill_rect)
    pygame.draw.rect(surf, WHITE, outline_rect, 2)


def create_orange():
    all_sprites.add(orange)
    
### Game loop ###
running = True
menu_screen = True


while running:
    # variables being kept track of at the start of the game.
    start_ticks = pygame.time.get_ticks()
    # Keep loop running at the right speed
    clock.tick(FPS)
    # Process input (events)
    if menu_screen:
        menu.show_menu_screen(screen, clock)
        menu_screen = False

    for event in pygame.event.get():
        if event.type == spawn_orange + 1:
            for i in range(cat.level):
                if cat.level > len(obstacle):
                    print(i)
                    o = Orange(POWER, 20, 15)
                    all_sprites.add(o)
                    obstacle.add(o)

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
                    cat.anger += 5
                    text_attitude.display_on(20)
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
                    cat.anger += 5
                    text_attitude.display_on(20)
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
                    cat.anger += 5
                    text_attitude.display_on(20)
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
                    cat.anger += 5
                    text_attitude.display_on(20)
                    changeDir = random.randint(1, 3)
                    if changeDir == 1:
                        cat.change_direction('bottom_left')
                    if changeDir == 2:
                        cat.change_direction('top_right')
                    if changeDir == 3:
                        cat.change_direction('top_left')


    # Message display if statements
    if cat.anger >= 100:
        cat.growl.play(fade_ms=1)
        # text_end_top.menu_show(screen)
        # text_end_bottom.menu_show(screen)
        # text.draw(screen)
        time.sleep(4)
        menu_screen = True
        bg.stop_music()
        bg.start_music()

    # Update
    all_sprites.update()
    click_boxes.update(cat)

    # Draw / render
    screen.fill(BLACK)
    screen.blit(bg.background, bg.rect)
    cattitude(screen, 350, 10, cat.anger)
    all_sprites.draw(screen)
    click_boxes.draw(screen)
    text.draw(screen)

    screen.blit(goal.sprite, goal.rect)
    screen.blit(cat.running_sprite, cat.rect)

    # Text checks
    text_ouch.display_check(screen)
    text_attitude.display_check(screen)

    # Collision Check for obstacles
    for unit in pygame.sprite.groupcollide(player, obstacle, False, True):
        text_ouch.display_on(20)
        angerRises()

    for unit in pygame.sprite.groupcollide(player, carrier, False, True):
        cat.level += 1
        print(cat.level)
        goal.respawn()
        carrier.add(goal)

    # *after* drawing everything, flip the display
    pygame.display.flip()


# Pygame end
pygame.mixer.quit()
pygame.quit()
