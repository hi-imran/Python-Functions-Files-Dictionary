def f(a, L=[]):
	L.append(a)
	return L

print(f(1))
print(f(2))
print(f(3))
print(f(4, ["Hello"]))
print(f(5, ["Hello"]))

"""
The second tricky thing is that if the default value is set to a mutable object, such as a list or a 
dictionary, that object will be shared in all invocations of the function. This can get very confusing,
so I suggest that you never set a default value that is a mutable object. For example, follow the 
exceution of this one carefully.
"""