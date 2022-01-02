olympians = [("John Aalberg", 31, "Cross Country Skiing"),
             ("Minna Maarit Aalto", 30, "Sailing"),
             ("Win Valdemar Aaltonen", 54, "Art Competitions"),
             ("Wakako Abe", 18, "Cycling")]

outfile = open("../myFiles/reduced_olympics.csv", "w")
# output the header row
outfile.write('Name,Age,Sport')
outfile.write('\n')
# output each of the rows:
for olympian in olympians:
    # row_string = (',').join(olympians) # when all values in olympians are string then we simply use this one
    #row_string = (',').join([olympian[0], str(olympian[1]), olympian[2]]) #Through join method, tangle approach
    row_string = '{},{},{}'.format(olympian[0], olympian[1], olympian[2]) #Recommanded way
    #row_string = olympian[0] + ',' + str(olympian[1]) + ',' + olympian[2] # Through concatination

    outfile.write(row_string)
    outfile.write('\n')
outfile.close()