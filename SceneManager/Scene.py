class Scene(object):
    
    def __init__(self, sceneName=None):
        self.sceneName = sceneName
        
    def set_name(self, stringValue):
        stringValueLength = len(stringValue)
        
        if(isinstance(stringValue, str)):
            if(stringValueLength < 15):
                self._sceneName = stringValue
            else:
                raise ValueError("String value out of bounds", "Bound: 15")
        else:
            raise ValueError("String value is not of type string")
        
    sceneName = property(set_name)
            
    
teste = Scene("MINHASCENA")
print(teste.sceneName)