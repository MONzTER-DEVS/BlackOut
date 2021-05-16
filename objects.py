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
        self.leg_back = LegIK(self.rect, 45)
        self.is_on_ground = False

    def render(self, window, scroll):
        window.blit(self.image, (self.rect.x - scroll.x, self.rect.y - scroll.y))
        self.leg_back.draw(window, scroll)

    def get_hits(self, tiles):
        return [tile for tile in tiles if self.rect.colliderect(tile.rect)]

    def move(self):
        if self.direction["left"]:
            self.vel.x = -self.strength
        elif self.direction["right"]:
            self.vel.x = self.strength
        else:
            self.vel.x = 0

        if self.direction["up"] and self.is_on_ground:
            self.vel.y = -2 * self.strength
            self.is_on_ground = False

    def update(self, tiles):
        self.leg_back.update(self.vel)
        self.vel.y += GRAVITY
        self.rect.x += self.vel.x
        # COLLISION ON X
        hits = self.get_hits(tiles)
        for tile in hits:
            if self.vel.x > 0:
                self.rect.right = tile.rect.left
                self.vel.x = 0
                if self.is_on_ground:
                    self.is_on_ground = False
            elif self.vel.x < 0:
                self.rect.left = tile.rect.right
                self.vel.x = 0
                if self.is_on_ground:
                    self.is_on_ground = False
        self.rect.y += self.vel.y
        # COLLISION ON Y
        hits = self.get_hits(tiles)
        for tile in hits:
            if self.vel.y > 0:
                self.is_on_ground = True
                self.rect.bottom = tile.rect.top
                self.vel.y = 0
            elif self.vel.y < 0:
                self.is_on_ground = False
                self.rect.top = tile.rect.bottom
                self.vel.y = 0


class Enemy:
    def __init__(self):
        self.image = pygame.Surface((16, 16))
        self.image.fill(color("#c46292"))
        self.rect = self.image.get_rect(center=(200, 100))
        self.vel = vec()
        self.direction = {
            "left": False,
            "right": False,
        }
        self.state = None
        self.strength = 5

    def render(self, window, scroll):
        window.blit(self.image, (self.rect.x - scroll.x, self.rect.y - scroll.y))

    def move(self):
        if self.direction['right']:
            self.vel.x = self.strength
        elif self.direction['left']:
            self.vel.x = -self.strength
        else:
            self.vel.x = 0

    def update(self):
        self.rect.x += self.vel.x


class Line:
    def __init__(self, origin: vec, width=1, **kwargs):
        self.origin = origin
        self.angular_speed = 0
        self.width = width
        if "end" in kwargs.keys():
            self.end = kwargs["end"]
            self.angle = self.origin.angle_to(self.end)
            self.components = vec(
                self.end.x - self.origin.x, self.end.y - self.origin.y
            )
            self.magnitude = self.components.magnitude()
        elif "angle" in kwargs.keys() and "magnitude" in kwargs.keys():
            self.angle = kwargs["angle"]
            self.magnitude = kwargs["magnitude"]
            self.end = vec()
            self.end.x = self.origin.x + self.magnitude * math.cos(
                math.radians(self.angle)
            )
            self.end.y = self.origin.y + self.magnitude * math.sin(
                math.radians(self.angle)
            )
            self.components = vec(
                self.end.x - self.origin.x, self.end.y - self.origin.y
            )
        else:
            raise_user_warning("Insufficient data for Line")

    def set_angle_from_origin(self, angle: float):
        self.angle = angle
        self.end.x = self.origin.x + self.magnitude * math.cos(math.radians(self.angle))
        self.end.y = self.origin.y + self.magnitude * math.sin(math.radians(self.angle))

    def set_angle_from_end(self, angle: float):
        self.angle = angle
        self.origin.x = self.end.x - self.magnitude * math.cos(math.radians(self.angle))
        self.origin.y = self.end.y - self.magnitude * math.sin(math.radians(self.angle))

    def rotate_from_origin(self, angle: float):
        self.angle += angle
        self.end.x = self.origin.x + self.magnitude * math.cos(math.radians(self.angle))
        self.end.y = self.origin.y + self.magnitude * math.sin(math.radians(self.angle))

    def rotate_from_end(self, angle: float):
        self.angle += angle
        self.origin.x = self.end.x - self.magnitude * math.cos(math.radians(self.angle))
        self.origin.y = self.end.y - self.magnitude * math.sin(math.radians(self.angle))

    def move_origin_to(self, pos: vec):
        self.origin = pos
        self.end.x = self.origin.x + self.magnitude * math.cos(math.radians(self.angle))
        self.end.y = self.origin.y + self.magnitude * math.sin(math.radians(self.angle))

    def move_end_to(self, pos: vec):
        self.end = pos
        self.origin.x = self.end.x - self.magnitude * math.cos(math.radians(self.angle))
        self.origin.y = self.end.y - self.magnitude * math.sin(math.radians(self.angle))

    def draw(self, screen, scroll):
        pygame.draw.line(
            screen,
            color(0, 0, 0),
            (self.origin - scroll),
            (self.end - scroll),
            self.width,
        )


# class Leg:
#     def __init__(self, body_rect: pygame.Rect, thigh_angle: float):
#         self.body_rect = body_rect
#         self.thigh = Line(vec(body_rect.bottomright), angle=thigh_angle, magnitude=25)
#         self.calf = Line(vec(self.thigh.end), angle=90, magnitude=25)

#     def update(self, vel: vec):
#         self.thigh.move_origin_to(vec(self.body_rect.midbottom))
#         self.calf.move_origin_to(self.thigh.end)
#         if vel.x > 0:  ## MOVING RIGHT
#             self.thigh.rotate_from_origin(vel.x * 2)
#             # self.calf.rotate_from_origin(5)
#         elif vel.x < 0:  ## MOVING LEFT
#             self.thigh.rotate_from_origin(vel.x * 2)
#             # self.calf.rotate_from_origin(-5)
#         if vel.y < 0:
#             self.calf.move_end_to(vec(self.calf.end.x, self.calf.end.y - 25))

#     def draw(self, screen, scroll):
#         self.thigh.draw(screen, scroll)
#         self.calf.draw(screen, scroll)


class LegIK:
    def __init__(self, body_rect: pygame.Rect, thigh_angle: float):
        self.body_rect = body_rect
        self.thigh = Line(vec(body_rect.bottomright), angle=thigh_angle, magnitude=25)
        self.calf = Line(vec(self.thigh.end), angle=90, magnitude=25)
        self.ik = vec(150, 100)
        self.joint_angle0 = 0
        self.joint_angle1 = 0

    def update(self, vel: vec):
        self.thigh.move_origin_to(vec(self.body_rect.midbottom))
        self.calf.move_origin_to(self.thigh.end)
        length0 = self.thigh.magnitude
        length1 = self.calf.magnitude
        length2 = self.calf.end.distance_to(self.thigh.origin)

        # mx, my = pygame.mouse.get_pos()
        # self.ik = vec(mx//2, my//2)
        # self.ik.x += 1
        # self.ik = vec(150, 100)

        diff = self.ik - self.thigh.origin
        atan = math.degrees(math.atan2(diff.y, diff.x))

        if length0 + length1 < length2:
            self.joint_angle0 = 135
            self.joint_angle1 = atan
        else:
            cosAngle0 = (
                (length2 * length2) + (length0 * length0) - (length1 * length1)
            ) / (2 * length2 * length0)
            angle0 = math.degrees(math.acos(cosAngle0))

            cosAngle1 = (
                (length1 * length1) + (length0 * length0) - (length2 * length2)
            ) / (2 * length1 * length0)
            angle1 = math.acos(cosAngle1)

            self.joint_angle0 = 135 - angle0
            self.joint_angle1 = atan - angle1

        # print(self.joint_angle0, self.joint_angle1)
        self.thigh.set_angle_from_origin(self.joint_angle0)
        self.calf.set_angle_from_origin(self.joint_angle1)

    def draw(self, screen, scroll):
        # self.ik.x -= scroll.x
        # self.ik.y -= scroll.y
        self.thigh.draw(screen, scroll)
        self.calf.draw(screen, scroll)
        pygame.draw.circle(screen, color(255, 255, 0), (self.ik - scroll), 10)
