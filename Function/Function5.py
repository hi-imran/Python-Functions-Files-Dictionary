def mylen(seq):
    c = 0 # initialize count variable to 0
    for _ in seq:
        c = c + 1   # increment the counter for each item in seq
    return c

print(mylen("hello"))
print(mylen([1, 2, 7]))
