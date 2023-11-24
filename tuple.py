# tuple is immutable, so can not be modified

'''
izzat = ('Izzat', 20, '10.04.2003')
print(izzat)
kiril = 'kiril', 19, '05.03.2004'
print(kiril)

tom = ('tom',) # for creating tuple with only one params should be , added
print(tom)

data = ['Tom', 20, '09.10.2003']
tomas = tuple(data)
print(tomas)
print(len(tomas)) # 3
print(tomas[1]) # 20

name, age, born = tomas
print(name)
print(age)
print(born)

print(tomas[:1]) # ('Tom',)
'''

'''
def getUserData():
    name = 'Izzat'
    age = 20
    born = '10.04.2003'
    return name, age, born

data = getUserData()

print(data) # tuple as result
'''

'''
def printInfo(name, age, height):
    print(f'Name: {name}, Age: {age}, Height: {height}')
    
userData = ('Izzat', 20)
printInfo(*userData, 170)
'''

'''
data = ('Kiril', 20, 180)
for item in data:
    print(item)
    
i = 0
while i < len(data):
    print(data[i])
    i+=1
'''

'''
data = ('Kiril', 20, 180)
name = 'Kiril'

if name in data:
    print('Is there')
else:
    print('doesnt there')
'''