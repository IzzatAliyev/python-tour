class Person:
    __type = 'Person'
    
    @staticmethod
    def printType():
        print(f'type is {Person.__type}')
        
person = Person()
person.printType() # without staticMethod annotation will be error
Person.printType()