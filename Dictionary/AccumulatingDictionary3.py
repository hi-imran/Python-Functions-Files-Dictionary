f = open('../myFiles/scarlet.txt', 'r')
txt = f.read()
# now txt is one long string containing all the characters
letter_counts = {} # start with an empty dictionary
letter_counts['t'] = 0  # initialize the t counter
letter_counts['s'] = 0  # initialize the s counter
for c in txt:
    if c == 't':
        letter_counts['t'] = letter_counts['t'] + 1  # increment the t counter
    elif c == 's':
        letter_counts['s'] = letter_counts['s'] + 1  # increment the s counter

print("t: " + str(letter_counts['t']) + " occurrences")
print("s: " + str(letter_counts['s']) + " occurrences")
