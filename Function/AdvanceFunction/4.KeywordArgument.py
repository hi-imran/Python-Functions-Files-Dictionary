initial = 7
def f(x, y = 3, z = initial):
    print("x, y, z are:", x, y, z)

f(2, x=5)

#Runtime error since two different values are provided for x