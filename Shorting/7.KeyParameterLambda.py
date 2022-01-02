L1 = [1, 7, 4, -2, 3]

def absolute(x):
    print("--- figuring out what to write on the post-it note for " + str(x))
    if x >= 0:
        return x
    else:
        return -x

print("About to call sorted")
L2 = sorted(L1, key=lambda x: absolute(x))
print("Finished execution of sorted")
print(L2)
"""
A lambda function is a small anonymous function.

A lambda function can take any number of arguments, but can only have one expression.
"""