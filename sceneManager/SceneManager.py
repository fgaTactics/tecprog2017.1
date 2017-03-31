from Scene import *

class SceneManager(object):
    
    curScene = Scene()
    gameSceneList = [curScene]
    
    def AddScene(self, newScene):
        self.gameSceneList.append(newScene)
    
    def RemoveScene(self, sceneName):
        sceneToRemove = self.FindScene(sceneName)
        self.gameSceneList.remove(sceneToRemove)
        if(sceneName == self.curScene.name):
            self.curScene = Scene()
    
    def LoadScene(self, sceneName):
        sceneToLoad = self.FindScene(sceneName)
        self.curScene = sceneToLoad
        
    def LoadNextScene(self):
        sceneListLength = len(self.gameSceneList)
        nextSceneIndex = self.gameSceneList.index(self.curScene)+1
        if(nextSceneIndex <= sceneListLength):
            LoadScene(self.gameSceneList[nextSceneIndex].name)
        else:
            raise ValueError("Next scene does not exists")
        
    def FindScene(self, sceneName):
        sceneListLength = len(self.gameSceneList)
        for scene in self.gameSceneList:
            sceneIndex = self.gameSceneList.index(scene)
            if(scene.name == sceneName):
                return scene
            elif(sceneIndex >= sceneListLength):
                raise ValueError("This scene does not exists")