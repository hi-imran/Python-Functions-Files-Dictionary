L2 = ["Cherry", "Apple", "Blueberry"]

L3 = sorted(L2) #sorted function returns a list and didnot change the original list.
print(L3)
print(sorted(L2))
print(L2) # unchanged

print("----")

L2.sort()
print(L2)
print(L2.sort())  #return value is None

print(sorted("Imran"))#sorted function works on immutable datatype also
"Imran".sort() #sort works only on list