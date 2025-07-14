import pygame
import random
from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS

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
        else:
            rand_angle = random.uniform(20, 50)
            new_pos_velocity = pygame.math.Vector2.rotate(self.velocity, rand_angle)
            new_neg_velocity = pygame.math.Vector2.rotate(self.velocity, -rand_angle)
            new_radius = self.radius - ASTEROID_MIN_RADIUS

            as1 = Asteroid(self.position.x, self.position.y, new_radius)
            as2 = Asteroid(self.position.x, self.position.y, new_radius)

            as1.velocity = new_pos_velocity * 1.2
            as2.velocity = new_neg_velocity * 1.2

    