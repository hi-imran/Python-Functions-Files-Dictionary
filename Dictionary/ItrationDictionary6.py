inventory = {'apples': 430, 'bananas': 312, 'oranges': 525, 'pears': 217}

print(inventory.get("apples"))
print(inventory.get("cherries"))

print(inventory.get("cherries",0))

"""
get("apples") = get["apple"]
but diff is that is 
get("apples") is not present in Dictionary then return None
get["apple"] will return error
get("cherries",0) takes two argument
"""