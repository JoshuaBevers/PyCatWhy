# Necessary imports
import pygame
import random
from init.gameinitalizers import *


class Cat(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((50, 50))
        self.image.fill(BLUE)
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH // 2, HEIGHT // 2)
        self.direction = "LEFT"

    def update(self):
        if self.direction == "LEFT":
            self.rect.x += 5
            if self.rect.right >= WIDTH:
                self.direction = "RIGHT"
        if self.direction == "RIGHT":
            self.rect.x -= 5
            if self.rect.left <= 0:
                self.direction = "LEFT"


# Space allocated for creating and adding variables.
cat = Cat()
all_sprites.add(cat)
clock = pygame.time.Clock()
all_sprites = pygame.sprite.Group()


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

    # Update

    all_sprites.update()

    # Draw / render
    screen.fill(BLACK)
    all_sprites.draw(screen)

    # *after* drawing everything, flip the display
    pygame.display.flip()

    # Get mouse button state and mouse position if pressed
    if pygame.mouse.get_pressed()[0]:
        mouse_coords = pygame.mouse.get_pos()
        mouse_position = [int(mouse_coords[0]), int(mouse_coords[1])]
        
        print(mouse_position)


# Pygame end
pygame.quit()
