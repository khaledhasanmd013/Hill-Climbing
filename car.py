import pygame

class Car:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.vy = 0
        self.speed = 5
        self.gravity = 0.5
        self.width = 50
        self.height = 30

    def move(self, keys):
        if keys[pygame.K_LEFT]:
            self.x -= self.speed
        if keys[pygame.K_RIGHT]:
            self.x += self.speed

    def apply_gravity(self, ground_y):
        self.vy += self.gravity
        self.y += self.vy
        
        if self.y + self.height >= ground_y:
            self.y = ground_y - self.height
            self.vy = 0

    def draw(self, screen):
        pygame.draw.rect(screen, (255, 0, 0), (self.x, self.y, self.width, self.height))
        pygame.draw.circle(screen, (0, 0, 0), (self.x + 10, self.y + self.height), 8)
        pygame.draw.circle(screen, (0, 0, 0), (self.x + self.width - 10, self.y + self.height), 8)
      
