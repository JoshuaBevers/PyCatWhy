# Necessary imports
import pygame
import random
from init.gameinitializers import *
from objects.cat import *
from objects.click_box import *

# Initialize pygame and create window
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("PyCatWhy?!")

# Space allocated for creating and adding variables.
cat = Cat()
top_left = Click_Box('top_left')
top_right = Click_Box('top_right')
bottom_left = Click_Box('bottom_left')
bottom_right = Click_Box('bottom_right')
clock = pygame.time.Clock()
all_sprites = pygame.sprite.Group()
click_boxes = pygame.sprite.Group()
all_sprites.add(cat)
click_boxes.add(top_left, top_right, bottom_left, bottom_right)

### Game loop ###
running = True
while running:
    # Keep loop running at the right speed
    clock.tick(FPS)
    # Process input (events)
    for event in pygame.event.get():
        # check for closing window
        if event.type == KEYDOWN and event.key == K_ESCAPE:
            running = False
        elif event.type == pygame.QUIT:
            running = False
        # clicking on cat
        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = event.pos
            if top_left.rect.collidepoint(x, y):
                cat.change_direction('top_left')
            if top_right.rect.collidepoint(x, y):
                cat.change_direction('top_right')
            if bottom_left.rect.collidepoint(x, y):
                cat.change_direction('bottom_left')
            if bottom_right.rect.collidepoint(x,y):
                cat.change_direction('bottom_right')
            

    # Update

    all_sprites.update()
    click_boxes.update(cat)

    # Draw / render
    screen.fill(BLACK)
    all_sprites.draw(screen)
    click_boxes.draw(screen)

    # *after* drawing everything, flip the display
    pygame.display.flip()

    # Get mouse button state and mouse position if pressed
    if pygame.mouse.get_pressed()[0]:
        mouse_coords = pygame.mouse.get_pos()
        mouse_position = [int(mouse_coords[0]), int(mouse_coords[1])]
        
        print(mouse_position)


# Pygame end
pygame.quit()
