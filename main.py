from imports import *
from scene_manager import SceneManager
from objects import Player, Line

pygame.init()

## SETTINGS
display_info = pygame.display.Info()
clock = pygame.time.Clock()
FPS = 60
SCALE = 1 / 2

WW, WH = 600, 400
WINDOW = pygame.display.set_mode((WW, WH))

SW, SH = WW * SCALE, WH * SCALE
display = pygame.Surface((SW, SH))

def main():
    ## SETUP
    player = Player()
    line = Line(vec(SW//2, SH//2), 1, angle=45, magnitude=50)
    ## MAIN LOOP
    while True:
        clock.tick(FPS)
        display.fill(color("#A5CBC3"))
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                manager.exit()
                return

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    player.direction["right"] = True
                if event.key == pygame.K_LEFT:
                    player.direction["left"] = True
                if event.key == pygame.K_UP:
                    player.direction["up"] = True
                # if event.key == pygame.K_SPACE:
                    # manager.change_scene(main)
                    # return
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT:
                    player.direction["right"] = False
                if event.key == pygame.K_LEFT:
                    player.direction["left"] = False
                if event.key == pygame.K_UP:
                    player.direction["up"] = False

        player.update()
        line.update()
        player.move()

        line.angular_speed += 0.5

        # line.angle += 1
        # line.origin.x += 5

        line.draw(display)
        player.render(display)
        WINDOW.blit(pygame.transform.scale(display, (WW, WH)), (0, 0))
        pygame.display.update()


manager = SceneManager(main)
manager.run()
