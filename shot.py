import pygame
from circleshape import CircleShape
from constants import *

# Initialize pygame
pygame.init()

class Shot(CircleShape):

    def __init__(self, x, y, rotate):
        super().__init__(x, y, SHOT_RADIUS)   

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, SHOT_RADIUS, 2)

    def update(self, dt):
        self.position += self.velocity * dt
