from Scene import *

class SceneManager(object):
    
    __gameSceneList = []
    curScene = Scene()
    
    def AddScene(self, newScene):
        gameSceneList.append(newScene)
    
    def RemoveScene(self, sceneName):
        sceneToRemove = FindScene(sceneName)
        gameSceneList.remove(sceneToRemove)
    
    def LoadScene(self, sceneName):
        sceneToLoad = FindScene(sceneName)
        curScene = sceneToLoad
        
    def LoadNextScene(self):
        sceneListLength = len(gameSceneList)
        nextSceneIndex = gameSceneList.index(curScene)+1
        if(nextSceneIndex <= sceneListLength):
            LoadScene(gameSceneList[nextSceneIndex].name)
        else:
            raise ValueError("Next scene does not exists")
        
    def FindScene(sceneName):
        sceneListLength = len(gameSceneList)
        for scene in gameSceneList:
            sceneIndex = gameSceneList.index(scene)
            if(scene.name == sceneName):
                return scene
            elif(sceneIndex >= sceneListLength):
                raise ValueError("This scene does not exists")