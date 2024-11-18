import pygame
import random
from constants import *
from circleshape import CircleShape
import random


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        new_angle = random.uniform(20,50)
        vect1_vel = self.velocity.rotate(new_angle)
        vect2_vel = self.velocity.rotate(-new_angle)
        astroids_new_radius = self.radius - ASTEROID_MIN_RADIUS
        astroid1 = Asteroid(self.position.x, self.position.y, astroids_new_radius)
        astroid2 = Asteroid(self.position.x, self.position.y, astroids_new_radius)
        astroid1.velocity = vect1_vel * 1.2
        astroid2.velocity = vect2_vel * 1.2



