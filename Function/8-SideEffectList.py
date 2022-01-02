def changeit(lst):
	lst[0] = "Michigan"
	lst[1] = "Wolverines"
	return lst

mylst = ['106', 'students', 'are', 'awesome']
newlst = changeit(mylst)
print(mylst)
print(newlst)