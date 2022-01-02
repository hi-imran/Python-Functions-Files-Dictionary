"""
If you remember, the .items() dictionary method produces a sequence of tuples. Keeping this in mind,
we have provided you a dictionary called pokemon. For every key value pair, append the key to the list
p_names, and append the value to the list p_number. Do not use the .keys() or .values() methods.

"""
pokemon = {'Rattata': 19, 'Machop': 66, 'Seel': 86, 'Volbeat': 86, 'Solrock': 126}
p_names = []
p_number = []
for names, number in pokemon.items():
    p_names.append(names)
    p_number.append(number)
print(p_names)
print(p_number)