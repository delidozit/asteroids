import pygame 
from circleshape import CircleShape
from pygame.math import Vector2
class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
    def draw(self, surface): 
        pygame.draw.circle(surface, (225, 225, 225), (self.position.x, self.position.y), self.radius, 2)
    def update(self, dt):
        self.position += self.velocity * dt