class Car:
    def __init__(self, name, price):
        self.__name = name
        self.__price = price
        
    @property
    def name(self):
        return self.__name  
    
    @name.setter
    def name(self, name):
        self.__name = name 
        
    @property
    def price(self):
        return self.__price
    
    @price.setter
    def price(self, price):
        self.__price = price
        
    def getInfo(self):
        print('{} {}'.format(self.__name, self.__price))
        
audi = Car('Audi', 20_000)
audi.getInfo()
audi.name = 'Audio'
audi.price = 25_999
print(audi.name)
print(audi.price)