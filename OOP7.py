class Employee:
    def __init__(self,name,age,salary):
        self.name = name
        self.age = age
        self.salary = salary
    
    def getName(self):
        return self.name
    
    def getAge(self):
        return self.age
    
    def getSalary(self):
        return self.salary
    
    def setSalary(self,value):
        self.salary = value

dude1 = Employee("John",33,25000)

print(dude1.getName())
print(dude1.getAge())
print(dude1.getSalary())

#We set a new salary
dude1.setSalary(26600)
#Check that the new salary has been updated
print(dude1.getSalary())
