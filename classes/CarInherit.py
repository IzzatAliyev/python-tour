class Vehicle:
    def __init__(self, name):
        self.__name = name

    def getInfo(self):
        print('Name: {}'.format(self.name))

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name


class Car(Vehicle):
    def isWorking(self):
        return True


motor = Vehicle('motor')
audi = Car('audi')
motor.getInfo()
audi.getInfo()
print(audi.isWorking())
