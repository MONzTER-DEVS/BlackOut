from imports import *


class Player:
    def __init__(self, image):
        self.image = image
        # commenting for now cause not having an image
        # self.rect = self.image.get_rect()
        self.vel = 8

    def render(self, window):
        # commenting for now cause not having an image
        # window.blit(self.image, self.rect)
        pygame.draw.rect(window, pygame.Color("#ffff66"), self.image)

    def move(self, direction):
        # self.image will change to self.rect when having an image
        if direction == "right":
            self.image.right += self.vel
        if direction == "left":
            self.image.left -= self.vel
        if direction == "up":
            self.image.top -= self.vel
        if direction == "down":
            self.image.bottom += self.vel
