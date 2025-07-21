import pygame.draw
from circleshape import CircleShape
from constants import (ASTEROID_MIN_RADIUS,
                       ASTEROID_MAX_RADIUS)
import random

class Asteroid(CircleShape):
	def __init__(self, x, y, radius):
		super().__init__(x, y, radius)

	def draw(self, screen):
		pygame.draw.circle(surface=screen, color='white', width=2, radius=self.radius, center=self.position)

	def update(self, dt):
		self.position += self.velocity * dt

	def split(self):
		self.kill()
		if self.radius <= ASTEROID_MIN_RADIUS:
			return
		random_angle = random.uniform(20, 50)
		vector_1 = self.velocity.rotate(random_angle)
		vector_2 = self.velocity.rotate(-random_angle)
		
		self.radius -= ASTEROID_MIN_RADIUS
		asteroid= Asteroid(self.position.x, self.position.y, self.radius)
		asteroid.velocity = vector_1 * 1.2

		asteroid = Asteroid(self.position.x, self.position.y, self.radius)
		asteroid.velocity = vector_2 * 1.2
