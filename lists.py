'''
numbers = [1,2,3,4,5]
letters = ['a', 'b', 'c', 'd']

# are equal
lists = list()
lists2 = []

objects = [1, 2.4, 'book', True]

print(numbers)
print(letters)
print(objects)
'''

'''
numbers = [1,2,3,4,5]
listNumbers = list(numbers)
print(listNumbers)

helloText = 'Hello'
listHelloLetters = list(helloText)
print(listHelloLetters)
'''

'''
numbers = [1] * 10
print(numbers) # [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]

strings = ['Kiril', "Tom"] * 5
print(strings) # ['Kiril', 'Tom', 'Kiril', 'Tom', 'Kiril', 'Tom', 'Kiril', 'Tom', 'Kiril', 'Tom']
'''
'''
peoples = ["Anton", "Kiril", "Tom", "Izzat"]
print(peoples[1])  # Kiril
print(peoples[-1])  # Izzat
print(peoples[-2])  # Tom
peoples[1] = "Soma"
print(peoples[1])  # Soma

anton, kiril, tom, izzat = peoples # count should equal
print(anton)
'''

'''
peoples = ["Anton", "Kiril", "Tom", "Izzat"]
for person in peoples:
    print(person)
    
i = 0
while i < len(peoples):
    print(peoples[i])
    i+=1
'''

'''
list1 = [1, 2, 3]
list2 = list([1, 2, 3])
if list1 == list2:
    print('equals')
else:
    print('not equal')
'''

'''
names = ["Anton",  "Kiril", "Tom", "Izzat"]
print(names[:2]) # :end index
print(names[1:3]) # start:end indexies
print(names[1:4:2]) # start:end:step
print(names[:-1]) # can also be
'''

'''
list = [1,2,3,4,5,6,7,8,9]
extendList = [45,24]
print(list)
list.append(10)
print(list) # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
list.insert(2, 9)
print(list) # [1, 2, 9, 3, 4, 5, 6, 7, 8, 9, 10]
list.extend(extendList)
print(list) # [1, 2, 9, 3, 4, 5, 6, 7, 8, 9, 10, 45, 24]
list.remove(2)
print(list) # [1, 9, 3, 4, 5, 6, 7, 8, 9, 10, 45, 24]
print(list.index(9)) # 1
print(list.pop(1)) # 9 deleteByIndex or without index will delete last element
print(list) # [1, 3, 4, 5, 6, 7, 8, 9, 10, 45, 24]
print(list.count(3)) # 1 count of 3
list.sort()
print(list) # [1, 3, 4, 5, 6, 7, 8, 9, 10, 24, 45]
list.reverse()
print(list) # [45, 24, 10, 9, 8, 7, 6, 5, 4, 3, 1]
copyList = list.copy()
print(copyList) # [45, 24, 10, 9, 8, 7, 6, 5, 4, 3, 1]

print(len(list)) # 11
print(sorted(list)) # [1, 3, 4, 5, 6, 7, 8, 9, 10, 24, 45]
print(list) # [45, 24, 10, 9, 8, 7, 6, 5, 4, 3, 1]
print(max(list)) # 45
print(min(list)) # 1
list.clear()
print(list) # []
'''

'''
people = ['Anton', 'Kiril', 'Tom', 'Artur', 'Izzat']

if 'Kiril' in people:
    print("Yes")
else:
    print('No')
    
del people[1]
print(people) # ['Anton', 'Tom', 'Artur', 'Izzat']
del people[:2]
print(people) # ['Artur', 'Izzat']
'''

'''
numbers = [2,4,1,4,5,6,2,3]
numbers[2:6] = [3,4] # change 
print(numbers) # [2, 4, 3, 4, 2, 3]
print(numbers.count(2)) # 2
numbers.sort()
print(numbers) # [2, 2, 3, 3, 4, 4]
numbers.sort(reverse=True)
print(numbers) # [4, 4, 3, 3, 2, 2]
numbers.sort(key=str.lower) # for sorting without register(for strings)
'''

'''
numbers = [1,2,3,4,5,6]
numbers2 = numbers
numbers2.append(7)
# are equal
print(numbers)
print(numbers2)

numbers3 = numbers.copy()
numbers3.append(8)
# are different
print(numbers)
print(numbers3)
'''

'''
numbers = [1,2,3]
numbers2 = [4,5,6]
numbers3 = numbers + numbers2
print(numbers3) # [1, 2, 3, 4, 5, 6]
'''

'''
numbers = [[1,2,3], [2,3,4], [5,6,7]]
print(numbers[0]) # [1, 2, 3]
print(numbers[0][1]) # 2
print(numbers)

subNumbers = [10,11]
subNumbers.append(12)
numbers.append(subNumbers)
print(numbers)

for subNum in numbers:
    for num in subNum:
        print(num)
'''
