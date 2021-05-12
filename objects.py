from imports import *


class Player:
    def __init__(self):
        self.image = pygame.Surface((32, 32))
        self.rect = self.image.get_rect()
        self.vel = vec()
        self.strength = 8

    def render(self, window):
        window.blit(self.image, self.rect)

    def move(self, direction):
        if direction == "right":
            self.vel.x = self.strength
            self.vel.y = 0
        elif direction == "left":
            self.vel.x = -self.strength
            self.vel.y = 0
        elif direction == "up":
            self.vel.y = -self.strength
            self.vel.x = 0
        elif direction == "down":
            self.vel.y = self.strength
            self.vel.x = 0

    def update(self):
        self.rect.x += self.vel.x
        self.rect.y += self.vel.y
