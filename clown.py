import pygame
import random

WINDOW_WIDTH = 1750
WINDOW_HEIGHT = 700

class Clown(object):

    def __init__(self):
        self.CLOWN_STARTING_VELOCITY = 3
        self.CLOWN_ACCELERATION = .5

        self.clown_velocity = self.CLOWN_STARTING_VELOCITY
        self.clown_dx = random.choice([-1, 1])
        self.clown_dy = random.choice([-1, 1])
        self.clown_image = pygame.image.load("clown.png")
        self.clown_rect = self.clown_image.get_rect()
        self.clown_rect.center = (WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2)

    def move(self):
        # Move the clown
        self.clown_rect.x += self.clown_dx * self.clown_velocity
        self.clown_rect.y += self.clown_dy * self.clown_velocity

        # Bounce the clown off the edges of the display
        if self.clown_rect.right >= WINDOW_WIDTH or self.clown_rect.left <= 0:
            self.clown_dx *= -1
        if self.clown_rect.top <= 0 or self.clown_rect.bottom >= WINDOW_HEIGHT:
            self.clown_dy *= -1
