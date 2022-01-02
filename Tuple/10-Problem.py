"""
The .items() method produces a sequence of key-value pair tuples. With this in mind, write code to create
a list of keys from the dictionary track_medal_counts and assign the list to the variable name track_events.
 Do NOT use the .keys() method.

"""
track_medal_counts = {'shot put': 1, 'long jump': 3, '100 meters': 2, '400 meters': 2, '100 meter hurdles': 3, 'triple jump': 3, 'steeplechase': 2, '1500 meters': 1, '5K': 0, '10K': 0, 'marathon': 0, '200 meters': 0, '400 meter hurdles': 0, 'high jump': 1}
track_events = []
for n in track_medal_counts.items():
    track_events.append(n[0])
print(track_events)