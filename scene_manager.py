from imports import *

"""

SCENE MANAGER MANUAL:
    SETUP:
        Step 1) create functions for each scene in which you need to have a scene loop.
            NOTE: you need to call manager.exit() and then "return" keyword in the next line to EXIT the game.

        Step 2) create an object of this class and pass in all the scene function names.
            NOTE: you can either put in a active_scene_index or specify it first
            (
                ex1: manager=SceneManager(game, main_menu, pause_menu)
                in this case, game will be the default scene

                ex2: manager= SceneManager(game, main_menu, pause_menu, active_scene_index=1)
                in this case, main_menu will be the default scene
            )

        Step 3) call manager.run() somewhere in your code, preferably at the bottom
    
    CHANGING SCENES:
        You can provide a scene function or an index to the scene in the manager.change_scene()
        then call "return".

    --------------------------------------------------------------------------------
    --------------------------------------------------------------------------------
    --------------- NOTE THAT THE "return" PART IS IMPORTANT AS HELL ---------------
    --------------------------------------------------------------------------------
    --------------------------------------------------------------------------------

    THIS MAY CONTAIN SOME SCENE TRANSITIONS IN THE FUTURE! ;)

"""


class SceneManager:
    def __init__(self, *scenes, active_scene_index=0):
        self.scenes = list(scenes)
        self.active_scene = self.scenes[active_scene_index]

    def run(self):
        while True:
            self.active_scene()

    def change_scene(self, scene=None, scene_index=None):
        if scene:
            self.active_scene = scene
        elif scene_index:
            self.active_scene = self.scenes[scene_index]
        else:
            raise_user_warning("NO SCENE CHANGED...")

    def exit(self):
        pygame.quit()
        sys.exit()
        return
