class PersonAgeException(Exception):
    def __init__(self, message):
        self.__message = message

    def __str__(self) -> str:
        return f'PersonAgeException: {self.__message}'


class Person:
    def __init__(self, name: str, age: int):
        self.__name = name
        self.__age = age
        
    @property
    def age(self):
        return self.__age


def checkPersonAge(person:Person):
    try:
        if person.age < 18:
            raise PersonAgeException('age is not enough')
        else:
            print('everything is OK')
    except PersonAgeException as ex:
        print(str(ex)) 
    finally:
        print('Function End')
        
        
person1 = Person('Izzat', 20)       
person2 = Person('Kiril', 17)       
checkPersonAge(person1)
checkPersonAge(person2)