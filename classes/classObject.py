# all classes inherite from object class

class Person:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age
        
    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self, name):
        self.__name = name
    
    @property
    def age(self):
        return self.__age
    
    @age.setter
    def age(self, age):
        self.__age = age
        
    def __str__(self) -> str:
        return f'Person: name = {self.name}, age = {self.age}'
    
    def __repr__(self) -> str:
        pass
        
person = Person('Izzat', 20)
print(person) # call __str__ method