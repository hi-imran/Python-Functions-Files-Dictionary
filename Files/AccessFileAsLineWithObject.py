fileref = open("olympics.txt", "r")
#lines = fileref.readlines() #creats list of sentence
for line in fileref:
    print(line.strip())
fileref.close()

"""
Here we can access whole file. But cann't access a chunk/slice of it because it is object not list.
"""