import pygame
import sys
from car import Car
from environment import Environment

pygame.init()

WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Hill Climbing Mini Game")
clock = pygame.time.Clock()

env = Environment(WIDTH, HEIGHT)
car = Car(100, 100)

running = True
while running:
    screen.fill((135, 206, 235))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    car.move(keys)

    current_ground = env.get_height(car.x + 25)
    car.apply_gravity(current_ground)

    env.draw(screen)
    car.draw(screen)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()
