"""The dictionary travel contains the number of countries within each continent that Jackie has
traveled to. Find the total number of countries that Jackie has been to, and save this number to the
variable name total. Do not hard code this!"""

travel = {"North America": 2, "Europe": 8, "South America": 3, "Asia": 4, "Africa":1, "Antarctica": 0, "Australia": 1}
total = 0
# way 1
# for countries in travel.values():
#     total = total + countries
# print(total)

#way 1
for continent in travel:
    total = total + travel[continent]
print(total)