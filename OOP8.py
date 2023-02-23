class Person:
    #Class Variables
    dna = '0XX0'
    rna = 'XXYY'
    def __init__(self,name,age):
        self._name = name
        self.age = age

    
    def getName(self):
        return self._name

#Object/Instance creation
dude1 = Person("John",33)

#Access Class variable
print(Person.dna)
print(Person.rna)

#Edit Class variable during runtime
Person.dna = 'X00X'
print('Edited dna',Person.dna)
Person.rna = 'XYYX'
print('Edited rna',Person.rna)

#Add attribute to an instance at runtime
dude1.birthday = '18/10/1984'
print(dude1.birthday)

#We confirm the attribute is instance-based, NOT Class based!
print('Belongs to instance:',dude1.birthday)
print(Person.birthday) #Returns an AttributeError!
