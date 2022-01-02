fileref = open("olympics.txt", "r")
lines = fileref.readlines()
print(len(lines))
for line in lines[:4]:
    print(line.strip())
fileref.close()

"""
Since \n is already there and print also add \n that's why for each line gap is increased so we used strip().
"""