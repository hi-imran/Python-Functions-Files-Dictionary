n = [0] * 12
for i in range(1,13):
    n[i-1] = i *12
outfile = open("../myFiles/Multiples of 12.csv", "w")
for j in range(0, len(n)):
    outfile.write(str(j+1) + ',' + str(n[j]))
    # +1 to j since the array starts at 0 and we start counting at 1
    outfile.write('\n')
outfile.close()