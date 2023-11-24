class Person:
    defaultName = 'default'
    type = 'Person'
    desc = "person instance"
    
    def __init__(self, name):
        if name:
            self.__name = name
        else:
            self.__name = Person.defaultName
            
        
    @property
    def name(self):
        return self.__name
    
    def printDefaultName(self):
        print(self.defaultName)
        
        
person = Person('Kiril')
person2 = Person('')
print(person.type)
print(person.desc)
print(person.name)
print(person2.name)
person2.printDefaultName()
person2.defaultName = 'test'
person2.printDefaultName()

Person.type = 'Personx'
Person.name = 'Person Name'
print(Person.name)
print(Person.type)
print(Person.desc)