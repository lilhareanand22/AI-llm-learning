
        
        
class AndroidDeveloer:
    @property
    def write_kotlin(self):
        print("Writing Kotin code")
        
   
class Employee(AndroidDeveloer):
    def __init__(self, name, experience, role):
        self.name = name
        self.experience = experience
        self.role = role
        
    def introduce(self):
        print(f"Hi, I am {self.name}. I am an {self.role} with {self.experience} years of experience")  
        
        
        
              
    
emp = Employee("Anand", 12, "Android Lead Developer")
print(emp.name)
print(emp.experience)
print(emp.role)  
emp.introduce() 
emp.write_kotlin