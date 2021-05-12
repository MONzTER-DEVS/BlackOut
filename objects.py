from imports import *


class Player:
    def __init__(self):
        self.image = pygame.Surface((16, 16))
        self.image.fill(color("#85CB33"))
        self.rect = self.image.get_rect(center=(200, 100))
        self.vel = vec()
        self.strength = 5
        self.direction = {
            "left": False,
            "right": False,
            "up": False,
        }

    def render(self, window):
        window.blit(self.image, self.rect)

    def move(self):

        if self.direction["left"]:
            self.vel.x = -self.strength
        elif self.direction["right"]:
            self.vel.x = self.strength
        else:
            self.vel.x = 0

        if self.direction["up"]:
            self.vel.y = -self.strength

    def update(self):
        self.vel.y += GRAVITY
        self.rect.x += self.vel.x
        self.rect.y += self.vel.y

        if self.rect.bottom > 200:
            self.vel.y = 0
            self.rect.bottom = 200


class Line:
    def __init__(self, origin: vec, width=1, **kwargs):
        self.origin = origin
        self.angular_speed = 0
        self.width = width
        if 'end' in kwargs.keys():
            self.end = kwargs['end']
            self.angle = self.origin.angle_to(self.end)
            self.components = vec(self.end.x - self.origin.x, self.end.y - self.origin.y)
            self.magnitude = self.components.magnitude()
        elif 'angle' in kwargs.keys() and 'magnitude' in kwargs.keys():
            self.angle = kwargs['angle']
            self.magnitude = kwargs['magnitude']
            self.end = vec()
            self.end.x = self.origin.x + self.magnitude*math.cos(math.radians(self.angle)) 
            self.end.y = self.origin.y + self.magnitude*math.sin(math.radians(self.angle)) 
            self.components = vec(self.end.x - self.origin.x, self.end.y - self.origin.y)
        else:
            raise_user_warning("Insufficient data for Line")

    def update(self):
        self.angle += self.angular_speed
        self.end.x = self.origin.x + self.magnitude*math.cos(math.radians(self.angle)) 
        self.end.y = self.origin.y + self.magnitude*math.sin(math.radians(self.angle))

    def draw(self, screen):
        pygame.draw.line(screen, color(0, 0, 0), self.origin, self.end, self.width)
        # pygame.draw.circle(screen, color(0, 0, 0), self.origin, self.width//2)
        # pygame.draw.circle(screen, color(0, 0, 0), self.end, self.width//2)
