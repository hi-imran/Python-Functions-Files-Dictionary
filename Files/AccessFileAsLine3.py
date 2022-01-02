olympicsfile = open("olympics.txt", "r")

for aline in olympicsfile.readlines():
    values = aline.split(",") #list of strings
    print(values[0], "is from", values[3], "and is on the roster for", values[4])
    print(values)
olympicsfile.close()

"""
To process all of our olypmics data, we will use a for loop to iterate over the lines of the file. 
Using the split method, we can break each line into a list containing all the fields of interest about 
the athlete. We can then take the values corresponding to name, team and event to construct a simple 
sentence.
"""