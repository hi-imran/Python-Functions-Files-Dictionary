"""Create a dictionary called d that keeps track of all the characters in the string placement and
notes how many times each character was seen. Then, find the key with the lowest value in this dictionary
and assign that key to min_value."""


placement = "Beaches are cool places to visit in spring however the Mackinaw Bridge is near. Most people visit Mackinaw later since the island is a cool place to explore."
d = {}

for each_char in placement:
    if each_char not in d:
        d[each_char] = 0
    d[each_char] = d[each_char] + 1

key_list = list(d.keys())
min_value = key_list[0]

for key in key_list:
    if d[min_value] > d[key]:
        min_value = key
print(min_value)

