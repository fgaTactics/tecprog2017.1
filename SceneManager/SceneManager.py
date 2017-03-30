from Scene import *

class SceneManager(object):
    
    __gameSceneList = []
    curScene = Scene()
    
    def AddScene(self, newScene):
        gameSceneList.append(newScene)
    
    def RemoveScene(self, sceneName):
        sceneToRemo = FindScene(sceneName)
        gameSceneList.remove(sceneToRemove)
        
    def FindScene(sceneName):
        sceneListLength = len(gameSceneList)
        for scene in gameSceneList:
            sceneIndex = gameSceneList.index(scene)
            if(scene.name == sceneName):
                return scene
            elif(sceneIndex >= sceneListLength):
                raise ValueError("This scene does not exists")