class Car:
    def __init__(self, name, model):
        self.name=name
        self.model=model
        
    def getInfo(self):
        print('{} {}'.format(self.name, self.model))
        
audi = Car('audi', 'c100')
audi.price = 20_000
print('{} {} {}'.format(audi.name, audi.model, audi.price))
print(audi)

bmw = Car('bmw', 'cx')
volkswagen = Car('volkswagen', 'xte')
bmw.getInfo()
volkswagen.getInfo()