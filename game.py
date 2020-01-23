import pygame
import random
from init.gameinitalizers import *
from objects.cat import Cat

clock = pygame.time.Clock()
all_sprites = pygame.sprite.Group()


               


# Space allocated for creating and adding variables.

cat = Cat()
all_sprites.add(cat)

# initialize pygame and create window
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("My Game")


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
