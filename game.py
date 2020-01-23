import pygame
import random
from init.gameinitalizers import *

clock = pygame.time.Clock()
all_sprites = pygame.sprite.Group()


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
