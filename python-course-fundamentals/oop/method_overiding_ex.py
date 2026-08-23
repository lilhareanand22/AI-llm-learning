
class Animal:
    def sound(self):
        print("Animal Sound")
        

class Dog(Animal):
    def sound(self):
        super().sound()
        print("Dog sound")
        
    
dog = Dog()
dog.sound()
()