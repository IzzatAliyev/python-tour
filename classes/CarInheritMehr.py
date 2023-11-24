class Vehicle:
    def __init__(self, name):
        self.__name = name

    def getInfo(self):
        print('Name: {}'.format(self.name))
        
    def flying(self):
        print('Vehicle: {}'.format(self.name))

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name
        
class Fly:
    def __init__(self, name):
        self.__name = name

    def getInfo(self):
        print('Name: {}'.format(self.name))
        
    def flying(self):
        print('Fly: {}'.format(self.name))

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name


class Car(Fly,Vehicle): # if Fly is first then audi.flying() is from Fly otherwise from Vehicle
    def isWorking(self):
        return True


motor = Vehicle('motor')
flyer = Fly('flyer')
audi = Car('audi')
motor.getInfo()
flyer.getInfo()
flyer.flying()
audi.getInfo()
audi.flying()
print(audi.isWorking())
