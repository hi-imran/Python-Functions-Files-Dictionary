fileconnection = open("olympics.txt", 'r')
lines = fileconnection.readlines() # creates a list of string from new line
header = lines[0]
field_names = header.strip().split(',')
print(field_names)
for row in lines[1:]:
     vals = row.strip().split(',')
     if vals[5] != "NA":
        print("{}: {}; {}".format(
                 vals[0],
                 vals[4],
                 vals[5]))