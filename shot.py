from circleshape import CircleShape
import pygame
from constants import SHOT_RADIUS

class Shot(CircleShape):
	def __init__(self, x, y):
		super().__init__(x, y, SHOT_RADIUS)

	def draw(self, screen):
		pygame.draw.circle(surface=screen, color='white', width=2, radius=self.radius, center=self.position)

	def update(self, dt):
		self.position += self.velocity * dt