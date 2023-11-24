
'''
# equal
x,y = 10,20
x,y = (10,20)
# k,m = 10 # error

print(x) # 10
print(y) # 20
'''
'''
name, age, height = ('Izzat', 20, 170)
print(name)
print(age)
print(height)
'''

'''
data = ['Izzat', 20, 180]

name, age, height = data
print(name)
print(age)
print(height)
'''

'''
dictin = {'id': 1, 'name': 'Izzat', 'height': 170}
id, name, height = dictin
print(id)
print(name)
print(height)
'''

'''
users = [
    ('Izzat', 20, 170),
    ('Anton', 30, 175),
    ('Kiril', 21, 180)
]

for name,age,height in users:
    print('Name : {}, Age : {}, Height : {}'.format(name, age, height))
'''

'''
peoples = ['Izzat', 'Anton', 'Andrey']

for index, name in enumerate(peoples):
    print(f'{index}.{name}')
'''
'''
data = ['Izzat', 12, 'Google']
name, _, company = data

print(name)
print(company)
print(_)
'''

# packing
'''
num1 = 1
num2 = 2
num3 = 3

*numbers, = num1, num2, num3
print(numbers) # [1, 2, 3]
'''

'''
numbers = [1,2,3,4,5,6]

num1, *numms = numbers
print(numms) # [2, 3, 4, 5, 6]
numF, *nummers, numL = numbers
print(nummers) # [2, 3, 4, 5]
'''

'''
numbers = {1:12, 2: 22, 3: 32}

num1, *nums = numbers
print(num1)
print(nums)
'''

'''
numbers1 = [1,2,3]
numbers2 = [4,5,6]

numbers3 = [numbers1, numbers2]
print(numbers3) # [[1, 2, 3], [4, 5, 6]]
numbers4 = [*numbers1, *numbers2]
print(numbers4) # [1, 2, 3, 4, 5, 6]
'''
'''
diction1 = {1:11, 2:22, 3:33}
diction2 = {4:44, 5:55, 6:66}

diction3 = {**diction1, **diction2}
print(diction3) # {1: 11, 2: 22, 3: 33, 4: 44, 5: 55, 6: 66}
'''