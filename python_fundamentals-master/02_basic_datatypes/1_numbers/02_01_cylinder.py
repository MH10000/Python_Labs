'''
Write the necessary code calculate the volume and surface area
of a cylinder with a radius of 3.14 and a height of 5. Print out the result.


'''
# Defining variables
r = 3.14
h = 5
import math # importing math library

# Calculating volume and surface area
volume = math.pi * (r ** 2) * h
surface_area = 2 * math.pi * r * (r + h)
 
 # Print result
print("The volume of the circle is " + str(volume) + " and the surface area is " + str(surface_area))

