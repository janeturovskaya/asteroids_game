import pygame.draw

from circleshape import CircleShape

class Asteroid(CircleShape):
	def __init__(self, x, y, radius):
		super().__init__(x, y, radius)

	def draw(self, screen):
		pygame.draw.circle(surface=screen, color='white', width=2, radius=self.radius, center=self.position)

	def update(self, dt):
		self.position += self.velocity * dt

		