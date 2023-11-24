class Car:
    def __init__(self, name, price):
        self.__name = name
        self.__price = price
        
    def setName(self, name):
        self.__name = name 
        
    def setPrice(self, price):
        self.__price = price
        
    def getName(self):
        return self.__name  
        
    def getPrice(self):
        return self.__price
        
    def getInfo(self):
        print('{} {}'.format(self.__name, self.__price))
        
audi = Car('Audi', 20_000)
audi.setName('Audio')
audi.setPrice(25_000)
audi.getInfo()
print(audi.getName())
print(audi.getPrice())