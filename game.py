import pygame
import random
from objects.cat import *

WIDTH = 780
HEIGHT = 780
FPS = 30

clock = pygame.time.Clock()
all_sprites = pygame.sprite.Group()
# Adds the cat to the field

# define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)


# Space allocated for classes >>>>>>> This should be added to its own file and inported at the top for cleaner code.
# This will hang around until we have a harder grasp on how pygame works.


               


# Space allocated for creating and adding variables.

cat = Cat()
all_sprites.add(cat)

# initialize pygame and create window
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("My Game")
clock = pygame.time.Clock()


# Game loop
running = True
while running:
    # keep loop running at the right speed
    clock.tick(FPS)
    # Process input (events)
    for event in pygame.event.get():
        # check for closing window
        if event.type == pygame.QUIT:
            running = False

    # Update

    all_sprites.update()

    # Draw / render
    screen.fill(BLACK)
    all_sprites.draw(screen)
    # *after* drawing everything, flip the display
    pygame.display.flip()

# Sprite Variables
cat = Cat()
all_sprites.add(cat)

pygame.quit()
