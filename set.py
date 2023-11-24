### set

'''
users = {'Izzat', 'kiril', 'andrey', 'anton', 'kiril'}

print(users) # {'andrey', 'Izzat', 'anton', 'kiril'} only unique

numbers = [1,2,3,4,5,5,6,7]

setNums = set(numbers)
print(setNums) # {1, 2, 3, 4, 5, 6, 7}

'''
'''
users = set() # empty set
users.add('Izzat')
users.add('Kiril')
print(users)
users.remove('Kiril')
print(users) # {'Izzat'}
# users.remove('Anton') # error
users.discard('Anton') # delete if exist otherwise nothing

users.clear()
'''
'''
numbers = {1,2,3,4,5,6,7,7,8}

for i in numbers:
    print(i)
    
copyNums = numbers.copy()
print(copyNums)
'''

'''
nums1 = {1,2,3,4,5,4,4}
nums2 = {7,6,6,5,5,8,10}

unionNums = nums1.union(nums2)
intersectionNums = nums1.intersection(nums2)
intersectionNums2 = nums1 & nums2 
differenceNums = nums1.difference(nums2)
differenceNums2 = nums1 - nums2
simmetricDifNum = nums1.symmetric_difference(nums2)
simmetricDifNum2 = nums1 ^ nums2
nums1.intersection_update(nums2)


print(unionNums) # {1, 2, 3, 4, 5, 6, 7, 8, 10}
print(intersectionNums) # {5} only what in beide sets exist
print(differenceNums) # {1, 2, 3, 4}
print(simmetricDifNum) # {1, 2, 3, 4, 6, 7, 8, 10}
print(nums1) # {5}
'''

'''
numsSub = {1,2,3}
numsSup = {1,2,3,4,5,7}

print(numsSub.issubset(numsSup)) # true
print(numsSup.issubset(numsSub)) # false

print(numsSup.issuperset(numsSub)) # true
print(numsSup.issuperset(numsSub)) # true
'''

# immutable set
'''
users = frozenset({'Izzat', 'Kiril', 'Anton'}) # cannot modified

print(len(users))
'''