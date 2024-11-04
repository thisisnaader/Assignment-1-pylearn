import math

radius = int(input())
Area = math.pow(radius, 2) * math.pi
#instead of math.pow(radius, 2) we can use "radius ** 2" or "radius * radius"
Perimeter = 2 * math.pi * radius 

print ("Area of circle is: ",Area)
print ("Perimeter of circle is: ",Perimeter)