initial = 7
def f(x, y = 3, z = initial):
    print ("x, y, z are:", x, y, z)
initial = 0
f(2)

#the default value for z is determined at the time the function is defined; at that time initial has the value 7.