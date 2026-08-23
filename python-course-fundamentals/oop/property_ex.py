
class User:
    def __init__(self, name):
        self._name = name
     
    @property   
    def getName(self):
        return self._name
    
    
user = User("Anand")
print(user.getName)