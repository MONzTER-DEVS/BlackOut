from imports import *
from scene_manager import SceneManager
from objects import Player, Line
from map_utility import load_map_by_csv

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
    player = Player(vec(SW // 2, SH // 2))
    line = Line(vec(SW // 2, SH // 2), 1, angle=45, magnitude=50)
    level, map_size = load_map_by_csv(os.path.join("maps", "map.csv"))
    scroll = vec()
    hit = None
    ## MAIN LOOP
    while True:
        clock.tick(FPS)
        display.fill(color("#A5CBC3"))
        scroll.x += (player.rect.centerx - scroll.x - SW / 2) // 10
        scroll.y += (player.rect.centery - scroll.y - SH / 2) // 10
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
        player.move()
        player.render(display, scroll)
        # line.angular_speed += 0.5
        # line.angle += 1
        # line.origin.x += 5
        # line.update()
        # line.draw(display)
        for tile in level:
            tile.draw(display, scroll)
            
        WINDOW.blit(pygame.transform.scale(display, (WW, WH)), (0, 0))
        pygame.display.update()


manager = SceneManager(main)
manager.run()
