opposites = {'up': 'down', 'right': 'wrong', 'true': 'false'}
acopy = opposites.copy()
acopy['right'] = 'left'

print(acopy is opposites)

print(opposites)
print(acopy)


"""
As you can see from the is operator, acopy and opposites refer to the different object.
"""