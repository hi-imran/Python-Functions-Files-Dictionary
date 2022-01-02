fileref = open("olympics.txt", "r")
contents = fileref.read() #creats myFiles as a one string
print(contents[:100])
fileref.close()

"""
Reads myFiles as string and print starting 100 character. This is important when we have need of chunk of file
instead of whole file.
"""