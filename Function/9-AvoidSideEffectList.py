def changeit(lst):
	lst[0] = "Michigan"
	lst[1] = "Wolverines"
	return lst

mylst = ['106', 'students', 'are', 'awesome']
newlst = changeit(list(mylst))
print(mylst)
print(newlst)

"""
The built-in list function, which takes a sequence as a parameter and returns a new list, works to copy
an existing list. For dictionaries, you can similarly call the dict function, passing in a dictionary to
get a copy of the dictionary back as a return value.
"""