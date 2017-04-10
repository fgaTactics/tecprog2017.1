from gameEngine.Scene import *


class SceneManager(object):

    # Scene that the game is showing to the player
    current_scene = Scene()

    game_scene_list = [current_scene]


    # Add a new scene to the game scene list
    def add_scene(self, new_scene):
        assert issubclass(type(new_scene), Scene), "The parameter is not a scene"
        scene_to_compare_name = Scene()
        scene_to_compare_name = self.find_scene(new_scene.name)

        # Check if exists a scene with the same name of the newScene
        if(scene_to_compare_name is None):
            self.game_scene_list.append(new_scene)
        else:
            raise ValueError("This name of scene already exists")


    # Remove a scene of the game
    def remove_scene(self, scene_name):
        assert type(scene_name) is str, "The parameter must be a string"
        scene_to_remove = self.find_scene(scene_name)

        """ Check if the scene to remove exists in the game
            and if it is the currentScene """
        if(scene_to_remove is not None):
            self.game_scene_list.remove(scene_to_remove)
            if(scene_name == self.current_scene.name):
                self.current_scene = Scene()
        else:
            raise ValueError("This scene does not exists")


    # Show a scene that exists in the game to the user
    def load_scene(self, scene_name):
        assert type(scene_name) is str, "The parameter must be a string"
        scene_to_load = Scene()
        scene_to_load = self.find_scene(scene_name)

        # Checks if the scene exists in the game
        if(scene_to_load is not None):
            self.current_scene = scene_to_load
        else:
            raise ValueError("This scene does not exists")


    # Show the next scene in the game scene list to the user
    def load_next_scene(self):
        scene_list_length = len(self.game_scene_list)
        next_scene_index = self.game_scene_list.index(self.current_scene) + 1

        # Check if the current scene is the last scene of the game
        if(next_scene_index <= scene_list_length):
            load_scene(self.game_scene_list[next_scene_index].name)
        else:
            raise ValueError("The current scene is the last scene")


    # Find a scene in the game scene list to use in others methods
    def find_scene(self, scene_name):
        assert type(scene_name) is str, "The parameter must be a string"
        scene_list_length = len(self.game_scene_list)

        for scene in self.game_scene_list:
            scene_index = self.game_scene_list.index(scene)

            if(scene.name == scene_name):
                return scene
            elif(scene_index >= scene_list_length):
                raise ValueError("This scene does not exists")
