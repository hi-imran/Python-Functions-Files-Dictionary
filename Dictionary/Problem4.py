"""Create a dictionary called lett_d that keeps track of all of the characters in the string
 product and notes how many times each character was seen. Then, find the key with the highest value in
 this dictionary and assign that key to max_value."""

product = "iphone and android phones"
lett_d = {}

for each_char in product:
    if each_char not in lett_d:
        lett_d[each_char] = 0
    lett_d[each_char] = lett_d[each_char] + 1

key_list = list(lett_d.keys())
max_value = key_list[0]

for key in key_list:
    if lett_d[max_value] < lett_d[key]:
        max_value = key
print(max_value)
