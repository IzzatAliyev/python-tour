# list comprehension

'''
numbers = [-3,-2,-1,0,1,2,3]
posNumbers = []

for i in numbers:
    if i > 0:
        posNumbers.append(i)
        
print(posNumbers) # [1, 2, 3]

posNumbers2 = [n for n in numbers if n>0]
print(posNumbers2) # [1, 2, 3]
'''

'''
numbers = [n for n in range(10)]
print(numbers) # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
'''

'''
dictionary = {1: 'red', 2: 'blue', 3: 'green'}

dictionary2 = [val for val in dictionary.values()]

print(dictionary2) # ['red', 'blue', 'green']
'''

'''
numbers = [-3, -2, -1, 0, 1, 2, 3]
numbersx2 = [n*2 for n in numbers]
numbersx22 = [n*2 if n > 0 else n for n in numbers]
print(numbersx2)  # [-6, -4, -2, 0, 2, 4, 6]
print(numbersx22)  # [-3, -2, -1, 0, 2, 4, 6]
'''

'''
words = {'name': 'Name', 'color': 'Farbe', 'hello': 'Hallo'}
words2 = [f'{key} {words[key]}' for key in words]
print(words2) # ['name Name', 'color Farbe', 'hello Hallo']
'''

'''
numbers = [n for n in range(10)]

numbers2 = [n for n in numbers if n % 2 == 0]

print(numbers2) # [0, 2, 4, 6, 8]
'''

'''
dictin = {1: 'hallo', 2: 'how', 3: 'why'}

dictinSort = [f'key: {dictio}' for dictio in dictin if len(dictin[dictio]) > 3 ]
print(dictinSort) # ['key: 1']
'''