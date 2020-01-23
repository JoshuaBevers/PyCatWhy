# Necessary imports
import pygame
import random
from init.gameinitializers import *
from objects.cat import Cat


               


# Space allocated for creating and adding variables.
cat = Cat()
clock = pygame.time.Clock()
all_sprites = pygame.sprite.Group()
all_sprites.add(cat)

# Initialize pygame and create window
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("PyCatWhy?!")

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
        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = event.pos
            if cat.rect.collidepoint(x,y):
                cat.change_direction()

    # Update
    all_sprites.update()

    # Draw / render
    screen.fill(BLACK)
    all_sprites.draw(screen)
    if cat.running_sprite == cat.running[0] and cat.rect.x % 50 == 0:
        cat.running_sprite = cat.running[1]
    elif cat.running_sprite == cat.running[1] and cat.rect.x % 50 == 0:
        cat.running_sprite = cat.running[0]
    screen.blit(cat.running_sprite, cat.rect)

    # *after* drawing everything, flip the display
    pygame.display.flip()


# Pygame end
pygame.quit()
