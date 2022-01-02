olympicsfile = open("olympics.txt", "r")

for aline in olympicsfile:
    values = aline.split(",")
    print(values[0], "is from", values[3], "and is on the roster for", values[4])

olympicsfile.close()

"""
To make the code a little simpler, and to allow for more efficient processing, Python provides a built-in
way to iterate through the contents of a file one line at a time, without first reading them all into a 
list. Some students find this confusing initially, so we don’t recommend doing it this way, until you get
a little more comfortable with Python. But this idiom is preferred by Python programmers, so you should
be prepared to read it. And when you start dealing with big myFiles, you may notice the efficiency gains
of using it.
"""