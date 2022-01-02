fname = "olympics.txt"
with open(fname, 'r') as md:
    for line in md:
        print(line)
# continue on with other code
"""
with open(fname, "r") as md:
    is equivalent to
md = open(fname, "r")
md.close()

"""