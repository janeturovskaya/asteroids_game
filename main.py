import pygame
from constants import (SCREEN_WIDTH,
                       SCREEN_HEIGHT,
                       ASTEROID_MIN_RADIUS,
                       ASTEROID_KINDS,
                       ASTEROID_SPAWN_RATE,
                       ASTEROID_MAX_RADIUS)

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    time = pygame.time.Clock()
    dt = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        screen.fill(color='black')
        pygame.display.flip()
        dt = time.tick(60) / 1000


if __name__ == "__main__":
    main()
