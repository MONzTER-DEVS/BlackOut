from imports import *
from scene_manager import SceneManager
from objects import Player, Line, Enemy
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
    player = Player()
    enemy = Enemy()
    level, map_size = load_map_by_csv(os.path.join("maps", "map.csv"))
    scroll = vec()
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
                    enemy.direction["right"] = True
                if event.key == pygame.K_LEFT:
                    player.direction["left"] = True
                    enemy.direction["left"] = True
                if event.key == pygame.K_UP:
                    player.direction["up"] = True
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT:
                    player.direction["right"] = False
                    enemy.direction["right"] = False
                if event.key == pygame.K_LEFT:
                    player.direction["left"] = False
                    enemy.direction["left"] = False
                if event.key == pygame.K_UP:
                    player.direction["up"] = False

        player.update(level)
        player.move()
        player.render(display, scroll)
        enemy.update()
        enemy.move()
        enemy.render(display, scroll)
        for tile in level:
            tile.draw(display, scroll)
        WINDOW.blit(pygame.transform.scale(display, (WW, WH)), (0, 0))
        pygame.display.update()


manager = SceneManager(main)
manager.run()
