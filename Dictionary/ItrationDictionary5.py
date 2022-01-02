inventory = {'apples': 430, 'bananas': 312, 'oranges': 525, 'pears': 217}
print('apples' in inventory)
print('cherries' in inventory)

if 'bananas' in inventory: # in operator works only on key
    print(inventory['bananas'])
else:
    print("We have no bananas")
"""
The first approach is to use the in and not in operators, which can test if a key is in the dictionary:
"""