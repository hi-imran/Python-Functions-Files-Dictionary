def circleInfo(r):
    """ Return (circumference, area) of a circle of radius r """
    c = 2 * 3.14159 * r
    a = 3.14159 * r * r
    return c, a # return (c,a)

print(circleInfo(10))

circumference, area = circleInfo(10)
print(circumference)
print(area)

circumference_two, area_two = circleInfo(45)
print(circumference_two)
print(area_two)
