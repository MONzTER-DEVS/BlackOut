from imports import *
from scene_manager import SceneManager
from objects import Player

pygame.init()

## SETTINGS
display_info = pygame.display.Info()
clock = pygame.time.Clock()
FPS = 60
SCALE = 1 / 2

WW, WH = display_info.current_w // 2, display_info.current_h // 2
WINDOW = pygame.display.set_mode((WW, WH))

SW, SH = WW * SCALE, WH * SCALE
display = pygame.Surface((SW, SH))


def main():
    ## SETUP

    ## MAIN LOOP
    while True:
        clock.tick(FPS)
        display.fill(pygame.Color("#09BC8A"))
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                manager.exit()
                return
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    manager.change_scene(some_other_scene)
                    return
        print("MAIN SCENE")

        WINDOW.blit(pygame.transform.scale(display, (WW, WH)), (0, 0))
        pygame.display.update()


def some_other_scene():
    ## SETUP
    player = Player()
    direction = None
    ## MAIN LOOP
    while True:
        clock.tick(FPS)
        display.fill(pygame.Color("#74B3CE"))
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                manager.exit()
                return
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    direction = "right"
                if event.key == pygame.K_LEFT:
                    direction = "left"
                if event.key == pygame.K_UP:
                    direction = "up"
                if event.key == pygame.K_DOWN:
                    direction = "down"
                if event.key == pygame.K_SPACE:
                    manager.change_scene(main)
                    return

        player.update()

        player.move(direction)
        print("SOME OTHER SCENE")

        WINDOW.blit(pygame.transform.scale(display, (WW, WH)), (0, 0))
        player.render(WINDOW)
        pygame.display.update()


manager = SceneManager(main, some_other_scene)
# while True:
manager.run()
