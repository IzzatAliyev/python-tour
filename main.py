import time

'''
print("hello")
print("smart")
if 2 > 2:
    print(True)
else:
    print(False)
'''

# it's comment

'''
it's 
block 
comment
'''

'''
print("My", "name", "is", "Izzat")
print("My", "name", "is", "Izzat", end='\n\n', sep=' and ')

name = input("Enter your name: ")
print("Your name is", name)
name = 'kiril'
print(name)
Name = 'anton'
print(name, 'und', Name, 'are different')
'''

'''
userName = 'Izzat'
lastName = 'Aliyev'
age = 20
isMale = True
print(userName, lastName, age, ', Male:', isMale)
'''

'''
print(0b1111)
print(0o1111)
print(0xFF)
print(f'{10:0x}') # convert dez -> hex
print(f'{10:0b}') # convert dez -> bin
print(hex(10)) # convert dez -> hex
print(oct(10)) # convert dez -> oct
print(bin(10)) # convert dez -> bin
name = 'izzat'
'''

'''
height = 1.7
weight = 75.23
pi = 3.14e3
pi2 = 3140e-3
we = 75,23
print(height)
print(weight)
print(pi)
print(pi2)
print(we)
'''

'''
math = 10+10j
print(math)
'''

'''
text = ("I'm Izzat"
        "I can read and sleep")
bigText = '''
# I'm Izzat
# I can read and sleep
'''

complexText = 'I can read \t read can i \'sometext\' \nread is cool '
print(text)
print(bigText)
print(complexText)
'''

'''
print(ord('h'))
data = '⭐'
print(data.encode())
'''

'''
path = 'C:\python\name2'
correctPath = r'C:\python\name2'
print(path)
print(correctPath)
'''

'''
userName = 'Izzat'
lastName = 'Aliyev'
age = 20
print(f'{userName} {lastName} {age}')
'''

'''
username = 'Izzat'
lastName = 'Aliyev'
print('{} {}'.format(username, lastName))
'''

'''
name = 'Izzat'
age = 17
isMale = True
weight = 72.5
print(type(name))
print(type(age))
print(type(isMale))
print(type(weight))
'''

'''
print("izzat", end=' and ')
print("aliyev")
'''

'''
plus = 5+5
minus = 10-5
multiply = 3*4
divide = 10/2
divide2 = 11/2
divide3 = 11//2
remainder = 11%2
powered = 11 ** 2
powered2 = pow(11, 2)

print(plus)
print(minus)
print(multiply)
print(divide)
print(divide2)
print(divide3)
print(remainder)
print(powered)
print(powered2)
'''
'''
num = 5 + 5 / 1 + 10 ** 2
print('The result is', num )
'''

'''
num = 5
num += 20
print(num)
'''

'''
print(round(3.23))
sometime = time.time()
sometime2 = time.time()
print(round(sometime2 - sometime))
'''

'''
num1 = 2.1
num2 = 0.001
print(f"{num1} plus {num2} equals to {num1 + num2}")
print(round(num1+num2)) # 2
print(round(num1 + num2, 2)) # 2.1
'''

'''
multiplying
print(f'{5:0b}') # 5 dex -> 101 bin
x = 2 # 010
y = 6 # 110
z = x & y # 010 -> 2
print(z)
'''

'''
return 1 if one of the bytes 1
x = 2 # 010
y = 6 # 110
z = x | y # 110 -> 6
print(z)
'''

'''
if equal then 0 otherwise 1
x = 2 # 010
y = 6 # 110
z = x ^ y # 100 -> 4
print(z)
'''

'''
def entcrypt(value, key):
    result = value ^ key
    print(result)


def deccrypt(value, key):
    result = value ^ key
    print(result)


entcrypt(100, 45)
deccrypt(73, 45)
'''

'''
x = 5
y = ~x # -(x+1)
print(y) 
'''
'''
a = 1
b = a >> 1   # 0
c = b << 1    # 0
'''

'''
a = 5
b = a >> 1   # 2
c = b << 1    # 4
'''

'''
a = 8
b = a >> 1   # 4
c = b << 1    # 8
'''

'''
if(True | False):
    print("True")

if(True or False):
    print("True")

if(True & False):
    print("True")

if(True and False):
    print("True")

if(True is not False):
    print("True")

if(True and False):
    print("True")

if(not True):
    print("True")

if(True != False):
    print("True")
'''


'''
helloText = 'gello'
text = 'Hello world'
if(helloText in text):
    print('Yes')
elif (helloText not in text):
    print("No")
'''

'''
name = 'izzat'
age = 20

if name == 'izzat':
    print("name is correct")
elif age == 20:
    print('age is correct')
else:
    print('nothing is correct')
'''

'''
day = 10
month = 12

if month == 1:
    print('correct month 1')
    if day == 1:
        print('correct day 1')
elif month == 12:
    print('correct month 12')
    if day == 1:
        print("correct day 1")
    elif day == 10:
        print('correct day 12')
    else:
        print('incorrect day')
else:
    print('incorrect month')
        
'''

'''
while_start = time.time()
age = 0
while age < 18:
    print('is not enought old', end=f'age is {age} \n')
    age += 1
else:
    print('is enought')
while_end = time.time()
while_result = while_end - while_start
print(f'start time is {while_start}')
print(f'end time is {while_end}')
print(f'result time is {while_result}')
'''

'''
name = 'Izzat'

for letter in name:
    print(letter, letter, letter, letter, end=f'{letter}\n', sep='')
else:
    print("end")
'''

'''
top = 1
bottom = 1

while top < 10:
    while bottom < 10:
        print(top * bottom, end='\t')
        bottom += 1
    print()
    bottom = 1
    top += 1
else:
    print('end')
'''

'''
for i in 'ba':
    for j in 'ab':
        print(f'{i}{j}')
'''

'''
for i in range(12): 
    print(i)
'''

'''
i = 1
while i < 10:
    i += 1
    if i == 5:
        continue # go to next iteration
    if i == 8:
        break # exit
    print(i)
'''

'''
def myPrint(text):
    print(text)
    
def sayHello(): print('hello')
    
myPrint('Hello World!')
myPrint('Hello World!')
myPrint('Hello World!')
sayHello()
sayHello()
sayHello()
'''

'''
def printer():
    print("I am a function")
    def helloher(): print('hellohen')
    def byebyer(): print('byebye')
    def howareyou(): print('how are you')
    
    helloher()
    howareyou()
    byebyer()
    print('ender')
    
printer()
'''

'''
def counter(value):
    print(value)
    counter(value+1)
    
counter(1)
'''

'''
def printInfo(name, age, isMale = True):
    print(f'Name: {name},Age: {age} is male? {isMale}')
printInfo('frederika',18, False)
printInfo('Izzat',20)
printInfo(name='Kiril', age=21)
'''

'''
def paramsByNameCall(*, name, age):
    print(f'{name} {age}')
    
# paramsByNameCall('izzat', 20) #error
paramsByNameCall(name='izzat', age=20)
'''

'''
def paramsByPositionCall(name, /, age, *, height):
    print(f'{name} {age} {height}')
    
# paramsByPositionCall('izzat', height=143, 20) #error
paramsByPositionCall('izzat', height=143, age=20)

'''

'''
def mySum(*numbers):
    print(sum(numbers))
    
mySum(1,2,3,4,5,6,7,8,9,10)
'''

'''
def getLetterByIndex(text, index):
    return text[index]

index = getLetterByIndex('Izzat', 3)
print(index)
'''

'''
def mySum(a, b):
    return a + b

print(mySum(5,3))
'''

'''
def printInfo(name, age):
    if age < 18:
        print('isn\'t old enought')
        return
    return f'{name} {age}'

print(printInfo('Izzat', 17))
'''

'''
def printMessage(text):print(text)
def printHello():print('Hello')

messager = printMessage
messager('Izzat')
messager = printHello
messager()
'''

'''
def printer():print('hello')
print(type(printer))
'''

'''
def doOperator(*nums, operation):
    result = operation(nums)
    return result

result = doOperator(3,2,3,4,5,operation=sum)
print(result)
'''

'''
def summ(*nums):
    print(sum(nums))
    
def multiply(*nums):
    sum=1
    for i in nums:
        sum *= i
    return sum

def selectOper(choice):
    if(choice == 1):
        return summ
    elif(choice == 2):
        return multiply
    else: return summ
    
def doOper(*nums, operation):
    result = operation(nums)
    return result

returnMethod = selectOper(2)
print(returnMethod(1,2,3,4,5))
'''

'''
summ = lambda n, b, d, g: n + b + d + g

print(summ(5,10, 3, 1))
'''

'''
square = lambda n: n*n
print(square(10))
'''

'''
def doOper(a,b, operation):
    oper = operation(a,b)
    return oper

result = doOper(1,2, operation= lambda *nums: sum(nums))
print(result)
'''

'''
def choiceOper(choice):
    if (choice==1):
        return lambda a, b: a+b
    elif choice == 2:
        return lambda a,b: a*b
    else:
        return lambda a,b: a+b
    
operation = choiceOper(1)
print(operation(1,2))
operation = choiceOper(2)
print(operation(1,2))
'''

'''
a = 2
b = 3.5
c = a+b
print(c)
'''

'''
a = '2'
b = 3.5
c = int(a)+b
print(c)
'''

'''
string = str(5)
print(string)
floa = float(5)
print(floa)
'''
'''
val = bool('true')
int(False) # 0
int(True) # 1
print(val)
'''

'''
val = 5
# print('num = ' + val) #error
print('num = ' + str(val)) 
'''

'''
name = 'Izzat'

def printName():
    print(name)

printName()
'''

'''
name = 'Izzat'

def printName():
    name = 'Kiril'
    print(name)

def printName2():
    print(name)
    
printName()
printName2() # Izzat
'''

'''
name = 'Izzat'

def printName():
    global name
    name = 'Kiril'
    print(name)

def printName2():
    print(name)
    
printName()
printName2() #Kiril
'''

'''
def outer():
    num=3
    def inner():
        num = 5
        print(num)
    print(num)
    inner()
    
outer() # 3
'''

'''
def outer():
    num=3
    def inner():
        nonlocal num
        num = 5
        print(num)
    inner()
    print(num)
    
outer() # 5
'''

'''
def outer():
    num=5
    def inner():
        nonlocal num
        num+=1
        print(num)
    return inner

inner = outer()
inner() #6
inner() #7
inner() #8
'''

'''
def multiply(n):
    def inner(m): return n*m
    return inner

operation = multiply(5)
print(operation(4))
print(operation(5))
print(operation(6))
'''

'''
def multiply(n):
    return lambda m: n*m

operation = multiply(5)
print(operation(4))
print(operation(5))
print(operation(6))
'''

'''
def check(func):
    def inner(*args):
        func(*args)
    return inner

@check
def printName(name, age):
    print(f'name is {name}, age is {age}')
    
printName('Izzat', 20)
'''

'''
def check(func):
    def inner(*args):
        name = args[0]
        age = args[1]
        if age < 18: age = 18 # upd if is not old enough
        func(name, age)
        print('hello')
    return inner

@check
def printInfo(name, age):
    print(f'name is {name}, age is {age}')

printInfo('Izzat', 8)
'''

'''
def check(func):
    def inner(*args):
        result = func(*args)
        if result < 0: result = 0
        return result
    return inner

@check
def sum(n1,n2):
    return n1 + n2

print(sum(3,-5))
'''

'''
class Test:
    pass

test = Test()
string = ' '

print(isinstance(test, Test))
print(isinstance(string, str))
'''
