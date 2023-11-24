
'''
keyvalue = {1:50, 2:60, 3:70}

print(keyvalue.get(2))

users = { 1: 'Izzat', 2:'Kiril', 3:'Andrey'}

for i in users.values():
    print (i)
    
objects = {1:True, '2': "Kril", 4:23.3 }

# equal
empty = {}
empty = dict()
'''
'''
userList = [
    ["izzat", "02131234323"],
    ["kiril", "23424324324"],
    ["anton", "23213343523"]
]

print(userList)
userDict = dict(userList)
print(userDict)

userTuple = (
    ("izzat", "02131234323"),
    ("kiril", "23424324324"),
    ("anton", "23213343523")
)

print(userTuple)
userDict2 = dict(userTuple)
print(userDict2)
'''
'''
users = {1: 100, 2: 200, 3: 300, 4: 400}

print(users[1])
users[2] = 222 # updated
print(users[2])
users[5] = 555 # added
print(users)
print(users[5])

if 1 in users:
    user = users[1]
    print(user)
else:
    print('doesn\'t exist')
'''
'''
users = {
    1:100,
    2:200,
    3:300
}

user1 = users.get(1)
user4 = users.get(4, 400) # if key 4 doesnt exist then will return default value 400
print(user4)

del users[2] # delete
print(users)
if 1 in users:
    del users[1]
    print(users)
else:
    print('doesn\'t find')
'''

'''
users = {
    1:100,
    2:200,
    3:300,
    4:400
}

deleted = users.pop(1) # delete and return deleted
deleted2 = users.pop(1, 0) # delete and return deleted if key doesnt exist then return default value
print(deleted)
print(deleted2)

users.clear()
print(users)
'''
'''
users = {
    1:100,
    2:300,
    3:400
}

userss = {
    4:400, 
    5:500,
    6:600
}

users2 = users.copy()

print(users) # {1: 100, 2: 300, 3: 400}
print(users2) # {1: 100, 2: 300, 3: 400}
users.update(users2) 
print(users) # {1: 100, 2: 300, 3: 400}
users.update(userss)
print(users) # {1: 100, 2: 300, 3: 400, 4: 400, 5: 500, 6: 600}
'''
'''
users = {
    1:100,
    2:200,
    3:300
}

for key in users:
    print(key)
    
for key, value in users.items():
    print(key, value)
    
for key in users.keys():
    print(key)
    
for value in users.values():
    print(value)
'''
'''
complexDict = {
    "Izzat": {
        "email": "izzat@mail.com",
        "age": 20
    }, 
    "Kiril": {
        "email": "kiril@mail.com",
        "age": 20
    },
    "Anton": {
        "email": "anton@mail.com",
        "age": 20
    }
}

print(complexDict["Izzat"]["email"]) # izzat@mail.com
print(complexDict["Anton"]) # {'email': 'anton@mail.com', 'age': 20}

key = 'email'

if key in complexDict["Izzat"]:
    print(complexDict["Izzat"][key])
else:
    print('doesnt exist')
'''