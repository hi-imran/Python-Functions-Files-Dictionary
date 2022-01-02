"""Create a dictionary called lett_d that keeps track of all of the characters in the string
 product and notes how many times each character was seen. Then, find the key with the highest value in
 this dictionary and assign that key to max_value."""

p = "Summer is a great time to go outside. You have to be careful of the sun though because of the heat."
low_d = {}

for each_char in p:
    if each_char not in low_d:
        each_char = each_char.lower()
        low_d[each_char] = 0
    low_d[each_char] = low_d[each_char] + 1
print(low_d)
