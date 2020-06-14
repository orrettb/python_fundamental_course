'''
Write the necessary code calculate the volume and surface area
of a cylinder with a radius of 3.14 and a height of 5. Print out the result.


'''
radius = 3.14
height = 5.

#formula for volume:
volume = 3.14 * (radius ** 2) * height
#formula for surface area: m
surface_area = (2 * 3.14 * radius * height) + (2 * 3.14 * (radius ** 2))
#print results
print(volume)
print(surface_area)