class Person:
    
    def __init__(self, name, age = 18):
        self.name = name
        self.age = age
    
    def getName(self):
        return self.name
    
    def sayName(self):
        return self.getName()

kiril = Person('Kiril', 19)
anton = Person('Anton')
print(kiril)
print(anton)
print(kiril.age)
print(anton.age)
anton.age = 21
print(anton.age)
print(kiril.getName())
print(anton.getName())
print(anton.sayName())