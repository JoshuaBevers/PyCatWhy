import pygame
import random
from init.gameinitializers import *


class Orange(pygame.sprite.Sprite):
    # Constructor. Pass in the color of the block,
    # and its x and y position
    def __init__(self, color, width, height):
        # Call the parent class (Sprite) constructor
        super().__init__()
        pygame.sprite.Sprite.__init__(self)
        # Create an image of the block, and fill it with a color.
        # This could also be an image loaded from the disk.
        self.image = pygame.Surface([width, height], pygame.SRCALPHA, 32)
        self.image.convert_alpha()
        pygame.draw.ellipse(self.image, color, [0, 0, width, height])
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(WIDTH)
        self.rect.y = random.randrange(HEIGHT)
        # Fetch the rectangle object that has the dimensions of the image
        # image.
        # Update the position of this object by setting the values
        # of rect.x and rect.y

        self.direction_x = "LEFT"
        self.direction_y = "UP"

    def update(self):
        if self.direction_x == "LEFT":
            self.rect.x += 5
            if self.rect.right >= WIDTH:
                self.direction_x = "RIGHT"
        if self.direction_x == "RIGHT":
            self.rect.x -= 5
            if self.rect.left <= 0:
                self.direction_x = "LEFT"
        if self.direction_y == "DOWN":
            self.rect.y += 5
            if self.rect.bottom >= HEIGHT:
                self.direction_y = "UP"
        if self.direction_y == "UP":
            self.rect.y -= 5
            if self.rect.top <= 0:
                self.direction_y = "DOWN"
