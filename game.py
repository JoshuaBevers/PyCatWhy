# Necessary imports
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
from objects.nanner import *
from objects.rage_bar import *
from objects.text import *
from pygame.locals import *
from objects.orange import *


# JOKE DEMO ERROR CODE
ohno = input(bcolors.WARNING +
             "File 'game.py', \n line 34 goal = Carrier() \n ^ \n SyntaxError: invalid syntax \n " + bcolors.ENDC + "Joshuas-MacBook-Pro:pygame joshuabevers$ ")

ohno = input(bcolors.WARNING +
             "File 'game.py', \n line 34 goal = Carrier() \n ^ \n SyntaxError: invalid syntax \n " + bcolors.ENDC + "Joshuas-MacBook-Pro:pygame joshuabevers$ ")


# Init setup
pygame.init()
pygame.mixer.init(44100, -16, 2, 2048)
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("PyCatWhy!?!")
clock = pygame.time.Clock()
running = True
menu_screen = True


# Variable setups
SPAWN_SPEED = 1000
top_left = Click_Box('top_left')
top_right = Click_Box('top_right')
bottom_left = Click_Box('bottom_left')
bottom_right = Click_Box('bottom_right')

text_ouch = Text("Meowch!", 30, FONT_WIDTH_CENTER, FONT_HEIGHT_TOP_T)
text_attitude = Text("This cat has attitude!", 30,
                     FONT_WIDTH_CENTER, FONT_HEIGHT_TOP_T+30)
text_end_top = Text("The cat has fucked off!", 50,
                    FONT_WIDTH_CENTER, FONT_HEIGHT_TOP_T)
text_end_bottom = Text("You lose.", 20, FONT_WIDTH_CENTER, FONT_HEIGHT_TOP_T)


# Event creation
spawn_orange = pygame.USEREVENT + 1
pygame.time.set_timer(spawn_orange + 1, SPAWN_SPEED)


# Space allocated for creating and adding variables.
bg = Background()
cattitude = Rage_Bar()
cat = Cat()
goal = Carrier()
menu = Menu(0)

# All sprites group set
all_sprites = pygame.sprite.Group()
all_sprites.add(cat)

# Obstacle group set
obstacle = pygame.sprite.Group()
banana = pygame.sprite.Group()

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
text.add(text_ouch, text_attitude, text_end_top, text_end_bottom)

# Start music!
bg.start_music()


# Create functions
def angerRises(num):
    cat.anger += num
    cat.screech.play(fade_ms=1)

def spawn_banana():
    b = Nanner(BANANA, 25, 24, cat)
    all_sprites.add(b)
    banana.add(b)

def create_orange():
    o = Orange(POWER, 20, 15, cat)
    all_sprites.add(o)
    obstacle.add(o)

def madCat():
    cat.growl.play(fade_ms=1)

def reset():
    cat.anger = 0
    cat.level = 0
    cat.end_game_sit = 0
    cat.direction_y = "UP"
    cat.direction_x = "LEFT"
    cat.running_sprite = cat.running_left[0]
    all_sprites.empty()
    all_sprites.add(cat)
    all_sprites.add(goal)
    obstacle.empty()
    banana.empty()
    menu.change_level_screen(cat.level)


### Game loop ###
while running:
    # Variables being kept track of at the start of the game.
    start_ticks = pygame.time.get_ticks()

    # Loop speed
    clock.tick(FPS)

    # Process input (events)
    if menu_screen:
        menu.show_menu_screen(screen, clock)
        menu_screen = False

    for event in pygame.event.get():
        if event.type == spawn_orange + 1:
            for i in range(cat.level):
                if cat.level >= 1:
                    if len(obstacle) < (cat.level + (cat.anger // 5)):
                        create_orange()
                if cat.level >= 3:
                    if len(banana) < (cat.level):
                        spawn_banana()

        if event.type == KEYDOWN and event.key == K_ESCAPE:
            running = False
        elif event.type == pygame.QUIT:
            running = False

        # Clicking on cat
        if event.type == pygame.MOUSEBUTTONDOWN and cat.direction_x != "STOP" and cat.direction_y != "STOP":
            attitude = random.randint(1, 15)
            x, y = event.pos
            if top_left.rect.collidepoint(x, y):
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
                else:
                    cat.change_direction('top_left', True)
            if top_right.rect.collidepoint(x, y):
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
                else:
                    cat.change_direction('top_right', True)
            if bottom_left.rect.collidepoint(x, y):
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
                else:
                    cat.change_direction('bottom_left', True)
            if bottom_right.rect.collidepoint(x, y):
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
                else:
                    cat.change_direction('bottom_right', True)

    # Message display if statements
    if cat.anger >= 100:
        if cat.end_game_sit == 0:
            madCat()
        cat.direction_y = "STOP"
        cat.direction_x = "STOP"
        cat.end_game_sit += 1
        if cat.end_game_sit == 120:
            menu.change_level_screen(-1)
            menu.show_menu_screen(screen, clock)
            reset()
            menu_screen = True

    # Update
    all_sprites.update()
    click_boxes.update(cat)

    # Draw / render
    screen.blit(bg.background, bg.rect)

    all_sprites.draw(screen)
    click_boxes.draw(screen)
    screen.blit(goal.sprite, goal.rect)
    screen.blit(cat.running_sprite, cat.rect)

    cattitude.draw_shield_bar(screen, cat)

    # Text checks
    text_ouch.display_check(screen)
    text_attitude.display_check(screen)

    # Collision Check for obstacles
    if cat.anger <= 100 and cat.direction_x != "STOP" and cat.direction_y != "STOP":
        for unit in pygame.sprite.groupcollide(player, obstacle, False, True):
            text_ouch.display_on(20)
            angerRises(5)
        for unit in pygame.sprite.groupcollide(player, banana, False, True):
            text_ouch.display_on(20)
            if cat.anger >= 95:
                angerRises(5)
            else:
                angerRises(10)

    for unit in pygame.sprite.groupcollide(player, carrier, False, True):
        cat.level += 1
        menu.change_level_screen(cat.level)
        if cat.level == 10:
            menu.show_menu_screen(screen, clock)
            reset()
        menu_screen = True

        goal.respawn(cat.rect.x, cat.rect.y)
        carrier.add(goal)

    # Flip the display
    pygame.display.flip()

# Pygame end
pygame.mixer.quit()
pygame.quit()
