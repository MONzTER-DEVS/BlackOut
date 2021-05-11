from imports import *
from scene_manager import SceneManager

pygame.init()

## SETTINGS
display_info = pygame.display.Info()
clock = pygame.time.Clock()
FPS = 60
SCALE = 1/2

WW, WH = display_info.current_w//2, display_info.current_h//2
WINDOW = pygame.display.set_mode((WW, WH))

SW, SH = WW*SCALE, WH*SCALE
display = pygame.Surface((SW, SH))

def main():
    ## SETUP

    ## MAIN LOOP
    while True:
        clock.tick(FPS)
        display.fill((255, 255, 255))
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                manager.exit()
                return
            if event.type == pygame.KEYDOWN:
                manager.change_scene(some_other_scene)
                return

        print("MAIN")

        WINDOW.blit(pygame.transform.scale(display, (WW, WH)), (0, 0))
        pygame.display.update()

def some_other_scene():
    ## SETUP

    ## MAIN LOOP
    while True:
        clock.tick(FPS)
        display.fill((255, 255, 255))
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                manager.exit()
                return
            if event.type == pygame.KEYDOWN:
                manager.change_scene(main)
                return

        print("SOME OTHER SCENE")

        WINDOW.blit(pygame.transform.scale(display, (WW, WH)), (0, 0))
        pygame.display.update()

manager = SceneManager(main, some_other_scene)
# while True:
manager.run()