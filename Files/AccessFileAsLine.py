fileref = open("olympics.txt", "r")
lines = fileref.readlines() #creats list of sentence
print(lines[:4])
fileref.close()

"""
This creats a list of sentence with ending line.so you can see \n after every sentence.
"""